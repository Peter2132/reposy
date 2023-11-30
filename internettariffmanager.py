import sqlite3

class InternetTariffManager:
    def __init__(self, db_path):
        self._db_path = db_path
        self._connection = sqlite3.connect(self._db_path)
        self._cursor = self._connection.cursor()
        self._selected_tariffs = []  

    def create_table(self):
        self._cursor.execute('''
            CREATE TABLE IF NOT EXISTS InternetTariffs (
                id INTEGER PRIMARY KEY,
                data_limit_gb TEXT,
                price INTEGER
            )
        ''')
        self._connection.commit()

    def insert_tariff(self):
        data_limit_gb = input("Введите лимит данных в гигабайтах: ")
        price = int(input("Введите стоимость тарифа в рублях: "))

        sql = "INSERT INTO InternetTariffs (data_limit_gb, price) VALUES (?, ?)"
        self._cursor.execute(sql, (data_limit_gb, price))
        self._connection.commit()
        print("Данные успешно добавлены в таблицу InternetTariffs.")

    def update_tariff_price(self, tariff_id, new_price):
        sql = "UPDATE InternetTariffs SET price = ? WHERE id = ?"
        self._cursor.execute(sql, (new_price, tariff_id))
        self._connection.commit()
        print("Цена тарифа успешно обновлена.")

    def delete_tariff(self, tariff_id):
        sql = "DELETE FROM InternetTariffs WHERE id = ?"
        self._cursor.execute(sql, (tariff_id,))
        self._connection.commit()
        print("Тариф успешно удален.")

    def filter_by_price(self, max_price):
        sql = "SELECT * FROM InternetTariffs WHERE price <= ?"
        self._cursor.execute(sql, (max_price,))
        data = self._cursor.fetchall()
        return data

    def choose_tariff(self, tariff_id):
        sql = "SELECT * FROM InternetTariffs WHERE id = ?"
        self._cursor.execute(sql, (tariff_id,))
        tariff = self._cursor.fetchone()
        if tariff:
            self._selected_tariffs.append(tariff)
            print(f"Тариф {tariff_id} успешно выбран.")
        else:
            print(f"Тариф с ID {tariff_id} не найден.")

    def generate_receipt(self, filename="C:\\Users\\trofi\\OneDrive\\Рабочий стол\\чек.txt"):
        total_amount = 0

        with open(filename, "w") as file:
            file.write("Список выбранных тарифов:\n")
            for tariff in self._selected_tariffs:
                try:
                    price = int(tariff[2])
                    total_amount += price
                    file.write(f"Тариф {tariff[0]}: {tariff[1]} GB - {price} руб.\n")
                except ValueError:
                    print(f"Ошибка преобразования цены: {tariff[2]} не является числом.")

            file.write("\nОбщая сумма: {} руб.".format(total_amount))

        
        self.remove_selected_tariffs()

        print(f"Чек успешно сгенерирован, сохранен в файле {filename} и выбранные тарифы удалены из базы данных.")

    def remove_selected_tariffs(self):
        for tariff in self._selected_tariffs:
            tariff_id = tariff[0]
            self.delete_tariff(tariff_id)

    def display_data(self):
        sql = "SELECT * FROM InternetTariffs"
        self._cursor.execute(sql)
        data = self._cursor.fetchall()
        for row in data:
            print(row)

    def close_connection(self):
        self._connection.close()