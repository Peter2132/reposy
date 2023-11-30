import sqlite3

from device import Device, Phone

from database1 import Database

from user import User

def main_menu():
    print("Выберите операцию:")
    print("1. Авторизация")
    print("2. Регистрация")
    print("3. Выйти")
    choice = input("Введите соответствующую цифру (1, 2 или 3): ")
    return choice

user_instance = User("", "", "")

while True:
    choice = main_menu()
    
    if choice == "1":
        authenticated = user_instance.authenticate()
        authenticated_role = user_instance.get_role()
        
        if authenticated:
            print(f"Добро пожаловать, {user_instance._username}!")
            break
        else:
            print("Авторизация не выполнена.")
    elif choice == "2":
        user_instance.register()
        print("Регистрация успешна!")
        break
    elif choice == "3":
        print("Программа завершена.")
        exit()
    else:
        print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")

user_instance = User("", "", "")


connection = sqlite3.connect("D:\\code piton\\НоваяПапка\\databse6.db")
cursor = connection.cursor()

from internettariffmanager import InternetTariffManager

db_path = "D:\\code piton\\НоваяПапка\\databse6.db"
tariff_manager = InternetTariffManager(db_path)

while True:
    print("\nМеню выбора операций:")
    if authenticated_role == "Сотрудник":
        print("1. Добавить тариф")
        print("2. Обновить цену тарифа")
        print("3. Удалить тариф")
        print("4. Фильтровать тарифы по цене")
    elif authenticated_role == "admin":
        print("5. Добавить роль пользователю")
        print("6. Просмотреть всех пользователей с ролью 'Сотрудник'")

    else:
        print("7. Выбрать тариф")
        print("8. Сгенерировать чек")
        print("9. Отобразить все данные")
        print("0. Выйти")

    choice = input("Выберите операцию (введите соответствующую цифру): ")

    if choice == "1"and authenticated_role == "Сотрудник":
        tariff_manager.insert_tariff()
    elif choice == "2"and authenticated_role == "Сотрудник":
        tariff_id = input("Введите ID тарифа для обновления цены: ")
        new_price = int(input("Введите новую цену: "))
        tariff_manager.update_tariff_price(tariff_id, new_price)
    elif choice == "3"and authenticated_role == "Сотрудник":
        tariff_id = input("Введите ID тарифа для удаления: ")
        tariff_manager.delete_tariff(tariff_id)
    elif choice == "4"and authenticated_role == "Сотрудник":
        max_price = int(input("Введите максимальную цену для фильтрации: "))
        filtered_data = tariff_manager.filter_by_price(max_price)
        print("Тарифы с ценой до {} рублей:".format(max_price))
        print(filtered_data)
    elif choice == "5" and authenticated_role == "admin":
        username_to_update = input("Введите имя пользователя, которому нужно добавить роль: ")
        new_role = input("Введите новую роль: ")
        user_instance.add_role_to_user(username_to_update, new_role)
        print(f"Роль {new_role} успешно добавлена пользователю {username_to_update}.")
    
    elif choice == "6" and authenticated_role == "admin":
        # Просмотр всех пользователей с ролью "Сотрудник"
        # Здесь нужно выполнить SQL-запрос для извлечения данных о пользователях с ролью "Сотрудник"
        cursor.execute("SELECT * FROM Users WHERE role = 'Сотрудник'")
        employees = cursor.fetchall()
        if employees:
            print("Пользователи с ролью 'Сотрудник':")
            for employee in employees:
                print(employee)  # Вывод информации о пользователях с ролью "Сотрудник"
        else:
            print("Нет пользователей с ролью 'Сотрудник'.")
         
    elif choice == "7":
        tariff_id = input("Введите ID тарифа для выбора: ")
        tariff_manager.choose_tariff(tariff_id)
    elif choice == "8":
        tariff_manager.generate_receipt()
    elif choice == "9":
        tariff_manager.display_data()
    elif choice == "0":
        tariff_manager.close_connection()
        break
    else:
        print("Некорректный ввод. Пожалуйста, выберите существующую операцию.")


cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
        id INTEGER PRIMARY KEY,
        username TEXT,
        password TEXT,
        role TEXT 
        )
    ''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Phones (
        id INTEGER PRIMARY KEY, 
        model TEXT,
        memory_type TEXT, 
        color TEXT, 
        manufacturer TEXT
        )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS InternetTariffs (
        id INTEGER PRIMARY KEY,
        data_limit_gb INTEGER,
        price INTEGER
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS MasterInHome (
        id INTEGER PRIMARY KEY,
        price TEXT
    )
''')
connection.commit()
connection.close()