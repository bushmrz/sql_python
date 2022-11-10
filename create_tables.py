import sqlite3
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

con = sql_connection()

sellers_table(con)
providers_table(con)
items_table(con)
transactions_table(con)
history_table(con)

