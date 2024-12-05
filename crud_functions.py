import sqlite3


def initiate_db():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создаем таблицу Users, если она не существует
    cursor.execute('''
           CREATE TABLE IF NOT EXISTS Users (
               id INTEGER PRIMARY KEY,
               username TEXT NOT NULL,
               email TEXT NOT NULL,
               age INTEGER NOT NULL,
               balance INTEGER NOT NULL DEFAULT 1000
           )
       ''')

    """products = [
        ('Product 1', 'Описание 1', 100),
        ('Product 2', 'Описание 2', 200),
        ('Product 3', 'Описание 3', 300),
        ('Product 4', 'Описание 4', 400)
    ]

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)"""
    connection.commit()
    connection.close()


def add_user(username, email, age):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Добавляем пользователя с балансовым значением по умолчанию 1000
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
                   (username, email, age, 1000))

    connection.commit()
    connection.close()


def is_included(username):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    # Проверяем, существует ли пользователь с данными имени
    cursor.execute('SELECT COUNT(*) FROM Users WHERE username = ?', (username,))
    count = cursor.fetchone()[0]

    connection.close()
    return count > 0

def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products
