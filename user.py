#user.py
import sqlite3
class User:
    def __init__(self, username, password, role):
        self._username = username
        self._password = password
        self._role = role
    def get_role(self):
        return self._role
    
    
    def authenticate(self):
        while True:
            try:
                input_username = input("Введите имя пользователя: ")
                # Проверяем, содержит ли ввод хотя бы один числовой символ
                if any(c.isdigit() for c in input_username):
                    raise ValueError("Имя пользователя не должно содержать цифры.")
                break
            except ValueError as ve:
                print(f"Ошибка: {ve}")
        
        while True:
            input_password = input("Введите пароль (только цифры): ")
            if input_password.isdigit():
                break
            else:
                print("Неверный формат пароля. Пожалуйста, введите только цифры.")
        
        connection = sqlite3.connect("D:\\code piton\\НоваяПапка\\databse6.db")
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT * FROM Users WHERE username = ? AND password = ?",
                           (input_username, input_password))
            user_data = cursor.fetchone()

            if user_data:
                print("Авторизация успешна!")
                self._username, self._password, self._role = user_data[1:]  
                return True
            else:
                print("Неверное имя пользователя или пароль.")
                return False

        except sqlite3.Error as e:
            print("Ошибка при выполнении SQL-запроса:", e)
            return False

        finally:
            connection.close()

    def register(self):
        self._username = input("Создать имя пользователя: ")
        self._password = input("Создать пароль: ")
        self._role = input("Создать роль пользователя: ")

    def validate_password(self, password):
        
        return len(password) >= 6
    
    def add_role_to_user(self, username, role):
        connection = sqlite3.connect("D:\\code piton\\НоваяПапка\\databse6.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE Users SET role = ? WHERE username = ?", (role, username))
        connection.commit()
        connection.close()

    def add_username_to_user(self, username):
        connection = sqlite3.connect("D:\\code piton\\НоваяПапка\\databse6.db")
        cursor = connection.cursor()
        cursor.execute("UPDATE Users SET username = ? WHERE username = ?", (username, username))
        connection.commit()
        connection.close()
        
    def register(self):
        while True:
            try:
                self.username = input("Создать имя пользователя: ")
                
                if not self.username.isalpha():
                    raise ValueError("Имя пользователя не должно содержать цифры.")
                break
            except ValueError as ve:
                print(f"Ошибка: {ve}")
        
        while True:
            try:
                self.password = input("Введите пароль (не должен содержать буквы): ")
                
                if self.password.isalpha() :
                    raise ValueError("Неверный формат пароля. ")
                break
            except ValueError as ve:
                print(f"Ошибка: {ve}")

        connection = sqlite3.connect("D:\\code piton\\НоваяПапка\\databse6.db")
        cursor = connection.cursor()

        try:
            cursor.execute("INSERT INTO Users (username, password) VALUES (?, ?)",
                           (self.username, self.password))
            connection.commit()
            print(f"Пользователь {self.username} успешно зарегистрирован.")

        except sqlite3.Error as e:
            print("Ошибка при выполнении SQL-запроса:", e)

        finally:
            connection.close()
