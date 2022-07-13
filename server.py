from flask import Flask, render_template, request, url_for, redirect, session
from werkzeug.utils import secure_filename
from sql import UsersDB


import os

def CREATE_DIRECTORY(id):
    try:
        os.mkdir(f'C:\\Users\\User\\Desktop\\PROJECTS\\OnlyRussians\\static\\images\\{id}')
        os.mkdir(f'C:\\Users\\User\\Desktop\\PROJECTS\\OnlyRussians\\static\\images\\{id}\\avatar')
        os.mkdir(f'C:\\Users\\User\\Desktop\\PROJECTS\\OnlyRussians\\static\\images\\{id}\\photos')
        return 1
    except FileExistsError:
        return 0 

def GET_PATH_TO_AVATAR(id):
    return f'C:\\Users\\User\\Desktop\\PROJECTS\\OnlyRussians\\static\\images\\{id}\\avatar'

def GET_PATH_TO_PHOTO(id):
    return f'C:\\Users\\User\\Desktop\\PROJECTS\\OnlyRussians\\static\\images\\{id}\\photos'


app = Flask(__name__)

users = UsersDB('users.db')

app.secret_key = f'GFJDGJ43G3$#@$#%@##!@J34POJGJREOGEWSFAWSF'


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

@app.route('/')
def index():
    session['error-file'] = ''
    session['error-login'] = ''
    session['error-register'] = ''
    session['del'] = ''
    session['error'] = ''
    session['information-user'] = ''
    return render_template('index.html', page_type = 'Главная')

@app.route('/login')
def login():
    session['error-file'] = ''
    session['error-register'] = ''
    return render_template('login.html', page_type = 'Авторизация', error = session['error-login'])

@app.route('/register')
def register():
    session['error-file'] = ''
    session['error-login'] = ''
    return render_template('reg.html', page_type = 'Регистрация', error = session['error-register'])

@app.route('/information')
def information():
    session['error-file'] = ''
    session['error-login'] = ''
    session['error-register'] = ''
    return render_template('information.html', page_type = 'О нас', information_text = 'Информация')

@app.route('/profile')
def profile():
    print(users.get_photos(session['information-user']['id']))
    try:
        session['error-login'] = ''
        session['error-register'] = ''
        session['information-user'] = users.get_info_user_through_name(session['information-user']['nickname'])
        return render_template('profile.html', profile_info=session['information-user'], page_type='Профиль', photo_len=len(session['information-user']['photos']), error = session['error-file'])
    except:
        return redirect('/login')

@app.route('/admin')
def admin():
    session['error-file'] = ''
    session['error-login'] = ''
    session['error-register'] = ''
    return render_template('admin.html', page_type='Админка', error = session['error'], dl = session['del'], profiles = users.get_all())

@app.route('/admin-del/<id>')
def admin_del(id):
    session['error-file'] = ''
    session['error'] = 'Success'
    #session['del'] = 'd'
    users.delete_user(id)
    return redirect('/admin')

@app.route('/check-login', methods=['POST'])
def check_login():
    if request.method == 'POST':
        login = request.form.get('nickname')
        password = request.form.get('password')
        req = {'nickname': login, 'password': password}
        if users.check_user_through_name(login):
            if users.check_user_password(req):
                session['information-user'] = users.get_info_user_through_name(login)
                session['error-login'] = ''
                return redirect(f'/profile')
            else:
                session['error-login'] = 'Неверный пароль!'
                return redirect('/login')
        else:
            session['error-login'] = 'Неверный логин!'
            return redirect('/login')

@app.route('/create-new-acc', methods=['POST'])
def create_new_account():
    if request.method == 'POST':
        req = {'name': request.form.get('login'), 'password': request.form.get('password'), 'email': request.form.get('email'), 'id': users.get_last_id()+1, 'admin': 0, 'online': 1, 'avatar': 'g', 'balance': 0, 'photos': 'Photos', 'nickname': request.form.get('nickname'), 'secondname': request.form.get('secondname'), 'description': 'Описание'}
        if users.check_user_through_name(request.form.get('nickname')):
            session['error-register'] = 'Это имя уже используется!'
            return redirect('/register')
        elif users.check_users_through_email(request.form.get('email')):
            session['error-register'] = 'Этот email занят!'
            return redirect('/register')
        else:
            session['error-register'] = ''
            users.write_info_user(req)
            CREATE_DIRECTORY(req['id'])
            return redirect('/login')

@app.route('/profile-edit-description', methods=['POST'])
def profile_edit():
    if request.method == 'POST':
        users.edit(session['information-user']['nickname'], 'description', request.form.get('description'))
        return redirect('/profile')

@app.route('/download-avatar', methods=['GET', 'POST'])
def download_avatar():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = f'{session["information-user"]["id"]}.{file.filename.split(".")[-1]}'
            app.config['UPLOAD_FOLDER'] = GET_PATH_TO_AVATAR(session['information-user']['id'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            users.edit(session['information-user']['nickname'], 'avatar', os.path.join(app.config['UPLOAD_FOLDER'], filename))
            session['information-user'] = users.get_info_user_through_name(session['information-user']['nickname'])

            return redirect('/profile')
        else:
            session['error-file'] = 'Ошибка при загрузке!'
            return redirect('/profile#download')

@app.route('/download-photo', methods=['GET', 'POST'])
def download_photo():
    if request.method == 'POST':
        file = request.files.get('file')
        if file:
            filename = secure_filename(file.filename)
            app.config['UPLOAD_FOLDER'] = GET_PATH_TO_PHOTO(session['information-user']['id'])
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            photos = users.get_photos(session['information-user']['id'])
            photos += f' {filename}'
            print(f'photos: {photos}')

            users.edit(session['information-user']['nickname'], 'photos', photos)
            session['information-user'] = users.get_info_user_through_name(session['information-user']['nickname'])

            return redirect('/profile')
        else:
            session['error-file'] = 'Ошибка при загрузке!'
            return redirect('/profile#download')

@app.route('/exit')
def exit():
    session['information-user'] = []
    return redirect('/login')

app.run()

