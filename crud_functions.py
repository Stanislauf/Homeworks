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
    """products = [
        ('Product 1', 'Описание 1', 100),
        ('Product 2', 'Описание 2', 200),
        ('Product 3', 'Описание 3', 300),
        ('Product 4', 'Описание 4', 400)
    ]

    cursor.executemany('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', products)"""
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT title, description, price FROM Products')
    products = cursor.fetchall()

    connection.close()
    return products