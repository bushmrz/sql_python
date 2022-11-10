import sqlite3
import datetime
from sqlite3 import Error

def sql_connection():
    try:
        con = sqlite3.connect('database.db')
        return con
    except Error:
        print(Error)

def sellers_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE sellers(seller_id integer PRIMARY KEY, "
        "name text, salary real, term_work text)")
    con.commit()

def providers_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE providers(provider_id integer PRIMARY KEY, prov_name text, works_time text, delivery_time text)")
    con.commit()

def items_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE items(item_id integer PRIMARY KEY, provider_id integer, item_name text, weight real,"
        " FOREIGN KEY (provider_id) REFERENCES providers_table (provider_id))")
    con.commit()

def transactions_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE transactions(trans_id integer PRIMARY KEY, provider_id integer,"
        "seller_id integer, cost real, date date,"
        "FOREIGN KEY (provider_id) REFERENCES providers_table (provider_id),"
        "FOREIGN KEY (seller_id) REFERENCES sellers_table (seller_id))")
    con.commit()

def history_table(con):
    cursorObj = con.cursor()
    cursorObj.execute(
        "CREATE TABLE history(note_id integer PRIMARY KEY, item_id integer, seller_id integer, create_info date,"
        "FOREIGN KEY (item_id) REFERENCES items_table (item_id),"
        "FOREIGN KEY (seller_id) REFERENCES sellers_table (seller_id))")
    con.commit()

def insert_info(con):
    cursorObj = con.cursor()

    cursorObj.execute("INSERT INTO sellers VALUES(1, 'Джо Байден', 300, '1 день')")
    cursorObj.execute("INSERT INTO sellers VALUES(2, 'Сергей Волков', 100, '15 лет')")
    cursorObj.execute("INSERT INTO sellers VALUES(3, 'Крутой продавец', 1000, '42 года')")
    cursorObj.execute("INSERT INTO providers VALUES(1, 'Дональд Трамп', '4 года', '1 день')")
    cursorObj.execute("INSERT INTO providers VALUES(2, 'Барак Обама', '4 года', '3 недели')")
    cursorObj.execute("INSERT INTO items VALUES(1, 1, 'Акции', 1432)")
    cursorObj.execute("INSERT INTO items VALUES(2, 1, 'Банковские карты', 0.045)")
    cursorObj.execute("INSERT INTO items VALUES(3, 2, 'Бензин', 1)")
    cursorObj.execute("INSERT INTO items VALUES(4, 2, 'Бумага', 5)")

    data = [(1, 1, 2, 50, datetime.date(2021,5,5))]
    data1 = [(2, 1, 1, 9999, datetime.date(2020,1,1))]
    data2 = [(3, 2, 3, 500, datetime.date(2022,12,12))]

    cursorObj.executemany("INSERT INTO transactions VALUES(?,?,?,?,?)", data)
    cursorObj.executemany("INSERT INTO transactions VALUES(?,?,?,?,?)", data1)
    cursorObj.executemany("INSERT INTO transactions VALUES(?,?,?,?,?)", data2)

    info = [(1, 1, 1, datetime.date(2022, 5, 5))]
    info1 = [(2, 2, 3, datetime.date(2022, 1, 2))]
    info2 = [(3, 3, 2, datetime.date(2022, 1, 1))]
    cursorObj.executemany("INSERT INTO history VALUES(?,?,?,?)", info)
    cursorObj.executemany("INSERT INTO history VALUES(?,?,?,?)", info1)
    cursorObj.executemany("INSERT INTO history VALUES(?,?,?,?)", info2)

    con.commit()

def update_table(con):
    cursorObj = con.cursor()
    cursorObj.execute('UPDATE sellers SET name = "Обычный продавец" where seller_id = 3')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE items SET weight = 50 where item_id = 4')
    con.commit()

    cursorObj = con.cursor()
    cursorObj.execute('UPDATE transactions SET cost = 5050 where cost < 9999')
    con.commit()

def delete_info(con):
    cursorObj = con.cursor()
    cursorObj.execute('DELETE from items where item_id = 4')
    con.commit()

def select_info(con):
    cursorObj = con.cursor()
    cursorObj.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table = cursorObj.fetchall()

    tablesList = []
    for tab in table:
        tablesList.append(tab[0])

    for listItem in tablesList:
        print(f"Вывод содержимого таблицы {listItem}")
        cursorObj.execute(f'SELECT * from {listItem}')
        [print(row) for row in cursorObj.fetchall()]

con = sql_connection()

# insert_info(con)

select_info(con)

# update_table(con)
# select_info(con)

# delete_info(con)
# select_info(con)
