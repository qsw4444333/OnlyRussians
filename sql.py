import sqlite3

class UsersDB(object):
    def __init__(self, db_file_name):
        self.connect = sqlite3.connect(db_file_name, check_same_thread=False)
        self.base_name = 'srtye32423fs423ghhgsgf42ssaefsdsgfd3243tjgh4trdstrgthjdtrtdsr'
        self.cursor = self.connect.cursor()
        self.cursor.execute(f'''CREATE TABLE IF NOT EXISTS {self.base_name}
                               (id INT, name TEXT, email TEXT, balance INT, avatar TEXT, online TEXT, password TEXT, admin BOOL, images TEXT, nickname TEXT, secondname TEXT, description TEXT)''')
        self.inquiry = {'name': 'admin', 'avatar': '', 'balance': 100, 'online': 1, 'id': self.get_last_id()+1, 'admin': 1, 'email': 'admin', 'password': 'admin', 'images': 'photos', 'secondname': '', 'nickname': '', 'description': 'Статус'}
        self.connect.commit()
        self.write_info_user(self.inquiry)
    def get_info_user_through_id(self, id):
        self.cursor = self.connect.cursor()
        self.inquiry['name'] = self.cursor.execute(f'''SELECT name FROM {self.base_name}
                                                      WHERE id = "{id}"''')
        self.inquiry['name'] = self.inquiry['name'].fetchall()[0][0]

        self.inquiry['avatar'] = self.cursor.execute(f'''SELECT avatar FROM {self.base_name}
                                                      WHERE id = "{id}"''')
        self.inquiry['avatar'] = self.inquiry['avatar'].fetchall()[0][0]

        self.inquiry['balance'] = self.cursor.execute(f'''SELECT balance FROM {self.base_name}
                                                      WHERE id = "{id}"''')
        self.inquiry['balance'] = self.inquiry['balance'].fetchall()[0][0]

        self.inquiry['online'] = self.cursor.execute(f'''SELECT online FROM {self.base_name}
                                                         WHERE id = "{id}"''')
        self.inquiry['online'] = self.inquiry['online'].fetchall()[0][0]

        self.inquiry['id'] = self.cursor.execute(f'''SELECT id FROM {self.base_name}
                                                     WHERE id = "{id}"''')
        self.inquiry['id'] = self.inquiry['id'].fetchall()[0][0]

        self.inquiry['admin'] = self.cursor.execute(f'''SELECT admin FROM {self.base_name}
                                                        WHERE id = "{id}"''')
        self.inquiry['admin'] = self.inquiry['admin'].fetchall()[0][0]

        self.inquiry['email'] = self.cursor.execute(f'''SELECT email FROM {self.base_name}
                                                        WHERE id = "{id}"''')
        self.inquiry['email'] = self.inquiry['email'].fetchall()[0][0]

        self.inquiry['password'] = self.cursor.execute(f'''SELECT password FROM {self.base_name}
                                                           WHERE id = "{id}"''')
        self.inquiry['password'] = self.inquiry['password'].fetchall()[0][0]

        self.inquiry['images'] = self.cursor.execute(f'''SELECT images FROM {self.base_name}
                                                        WHERE id = "{id}"''')
        self.inquiry['images'] = self.inquiry['images'].fetchall()[0][0]

        self.inquiry['secondname'] = self.cursor.execute(f'''SELECT secondname FROM {self.base_name}
                                                           WHERE id = "{id}"''')
        self.inquiry['secondname'] = self.inquiry['secondname'].fetchall()[0][0]

        self.inquiry['description'] = self.cursor.execute(f'''SELECT description FROM {self.base_name}
                                                           WHERE id = "{id}"''')
        self.inquiry['description'] = self.inquiry['description'].fetchall()[0][0]

        self.connect.commit()
        return self.inquiry

    def get_info_user_through_name(self, username):
        self.cursor = self.connect.cursor()
        self.inquiry['name'] = self.cursor.execute(f'''SELECT name FROM {self.base_name}
                                                       WHERE nickname = "{username}"''')
        self.inquiry['name'] = self.inquiry['name'].fetchall()[0][0]

        self.inquiry['nickname'] = username

        self.inquiry['avatar'] = self.cursor.execute(f'''SELECT avatar FROM {self.base_name}
                                                         WHERE nickname = "{username}"''')
        self.inquiry['avatar'] = self.inquiry['avatar'].fetchall()[0][0]

        self.inquiry['balance'] = self.cursor.execute(f'''SELECT balance FROM {self.base_name}
                                                          WHERE nickname = "{username}"''')
        self.inquiry['balance'] = self.inquiry['balance'].fetchall()[0][0]

        self.inquiry['online'] = self.cursor.execute(f'''SELECT online FROM {self.base_name}
                                                         WHERE nickname = "{username}"''')
        self.inquiry['online'] = self.inquiry['online'].fetchall()[0][0]

        self.inquiry['id'] = self.cursor.execute(f'''SELECT id FROM {self.base_name}
                                                     WHERE nickname = "{username}"''')
        self.inquiry['id'] = self.inquiry['id'].fetchall()[0][0]

        self.inquiry['admin'] = self.cursor.execute(f'''SELECT admin FROM {self.base_name}
                                                        WHERE nickname = "{username}"''')
        self.inquiry['admin'] = self.inquiry['admin'].fetchall()[0][0]

        self.inquiry['email'] = self.cursor.execute(f'''SELECT email FROM {self.base_name}
                                                        WHERE nickname = "{username}"''')
        self.inquiry['email'] = self.inquiry['email'].fetchall()[0][0]

        self.inquiry['password'] = self.cursor.execute(f'''SELECT password FROM {self.base_name}
                                                           WHERE nickname = "{username}"''')
        self.inquiry['password'] = self.inquiry['password'].fetchall()[0][0]
        
        self.inquiry['images'] = self.cursor.execute(f'''SELECT images FROM {self.base_name}
                                                        WHERE nickname = "{username}"''')
        self.inquiry['images'] = self.inquiry['images'].fetchall()[0][0]

        self.inquiry['secondname'] = self.cursor.execute(f'''SELECT secondname FROM {self.base_name}
                                                           WHERE nickname = "{username}"''')
        self.inquiry['secondname'] = self.inquiry['secondname'].fetchall()[0][0]

        self.inquiry['description'] = self.cursor.execute(f'''SELECT description FROM {self.base_name}
                                                           WHERE nickname = "{username}"''')
        self.inquiry['description'] = self.inquiry['description'].fetchall()[0][0]

        self.connect.commit()
        return self.inquiry

    def get_photos(self, id):
        self.cursor = self.connect.cursor()
        user = self.cursor.execute(f'''SELECT images FROM {self.base_name}
                                       WHERE id = "{id}"''').fetchall()[0][0]
        self.connect.commit()
        print(user)
        return user

    def check_user_through_name(self, username):
        self.cursor = self.connect.cursor()
        user = self.cursor.execute(f'''SELECT name FROM {self.base_name}
                                        WHERE nickname = "{username}"''')
        user = self.cursor.fetchall()
        self.connect.commit()
        if len(user) > 0:
            return True
        else:
            return False

    def check_user_through_id(self, id):
        self.cursor = self.connect.cursor()
        try:
            id = self.cursor.execute(f'''SELECT name FROM {self.base_name}
                                           WHERE id = "{id}"''')                 # Type = STRING
            id = self.cursor.fetchall()
            result = True
        except:
            result = False
        self.connect.commit()
        return result

    def check_user_password(self, info):
        self.cursor = self.connect.cursor()
        password_user = self.cursor.execute(f'''SELECT password FROM {self.base_name}
                                                WHERE nickname = "{info["nickname"]}"''').fetchall()
        if len(password_user) > 0:
            self.connect.commit()
            if str(password_user[0][0]) == str(info['password']):
                return True
            else:
                return False
        else:
            return False

    def check_users_through_email(self, email):
        self.cursor = self.connect.cursor()
        email = self.cursor.execute(f'''SELECT email FROM {self.base_name}
                                        WHERE email = "{email}"''').fetchall()
        self.connect.commit()
        if len(email) > 0:
            return True
        else:
            return False

    def check_user_admin(self, username):
        self.cursor = self.connect.cursor()
        try:
            admins =  self.cursor.execute(f'''SELECT admin FROM {self.base_name}
                                              WHERE name = "{username}"''')
            admins = self.cursor.fetchall()[0][0]
            if admins:
                result = True
            else:
                result = False
        except:
            result = False
        self.connect.commit()
        return result

    def edit(self, nickname, name, value):
        self.cursor = self.connect.cursor()
        self.cursor.execute(f'''UPDATE {self.base_name} SET {name} = "{value}" WHERE nickname = "{nickname}"''')
        self.connect.commit()

    def delete_user(self, id):
        self.cursor = self.connect.cursor()
        self.cursor.execute(f'''DELETE FROM {self.base_name} WHERE id = {id}''')
        self.connect.commit()

    def write_info_user(self, info):
        self.cursor = self.connect.cursor()
        self.cursor.execute(f'''INSERT INTO {self.base_name} (name, avatar, balance, online, id, admin, password, email, nickname, secondname, images, description) values("{info["name"]}", "{info["avatar"]}", {info["balance"]}, {info["online"]}, {info["id"]}, {info["admin"]}, "{info["password"]}", "{info["email"]}", "{info['nickname']}", "{info['secondname']}", "{info["images"]}", "Описание")''')
        self.connect.commit()

    def get_last_id(self):
        self.cursor = self.connect.cursor()
        lastId = self.cursor.execute(f'''SELECT id FROM {self.base_name}
                                        WHERE id=(SELECT MAX(id) FROM {self.base_name})''')
        lastId = self.cursor.fetchall()
        if len(lastId) > 0:
            return lastId[0][0]
        else:
            return 0

    def get_admins(self):
        self.cursor = self.connect.cursor()
        users = self.cursor.execute(f'''SELECT name FROM {self.base_name}
                                       WHERE admin = True''')
        users = self.cursor.fetchall()
        return users

    def get_online(self):
        self.cursor = self.connect.cursor()
        online = self.cursor.execute(f'''SELECT name FROM {self.base_name}
                                        WHERE online = True''')
        online = self.cursor.fetchall()
        return online

    def get_all(self):
        self.cursor = self.connect.cursor()
        all =  self.cursor.execute(f'''SELECT * FROM {self.base_name}''')
        all = self.cursor.fetchall()
        return all

    def connect_close(self):
        self.connect.close()
