import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

"""cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users_data = [
    ('User 1', 'example1@gmail.com', 10, 1000),
    ('User 2', 'example2@gmail.com', 20, 1000),
    ('User 3', 'example3@gmail.com', 30, 1000),
    ('User 4', 'example4@gmail.com', 40, 1000),
    ('User 5', 'example5@gmail.com', 50, 1000),
    ('User 6', 'example6@gmail.com', 60, 1000),
    ('User 7', 'example7@gmail.com', 70, 1000),
    ('User 8', 'example8@gmail.com', 80, 1000),
    ('User 9', 'example9@gmail.com', 90, 1000),
    ('User 10', 'example10@gmail.com', 100, 1000)
]

cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)

# Обновление balance у каждой 2-й записи начиная с 1-й
for i in range(1, 11, 2):
    cursor.execute('UPDATE Users SET balance = 500 WHERE id = ?', (i,))

# Удаление каждой 3-й записи начиная с 1-й
for i in range(1, 11, 3):
    cursor.execute('DELETE FROM Users WHERE id = ?', (i,))

# Выборка всех записей, где возраст не равен 60
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
results = cursor.fetchall()

# Вывод результатов в консоль
for username, email, age, balance in results:
    print(f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')

# Подсчет количества записей в таблице
cursor.execute('SELECT COUNT(*) FROM Users')
record_count = cursor.fetchone()[0]
print(f'Количество записей в базе данных: {record_count}')"""

# Здесь удалим запись с id = 6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчёт общего количества записей в таблице
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчёт суммы всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вывод среднего баланса всех пользователей
if total_users > 0:
    average_balance = all_balances / total_users
else:
    average_balance = 0

print(f'Средний баланс всех пользователей: {average_balance}')

conn.commit()
conn.close()
