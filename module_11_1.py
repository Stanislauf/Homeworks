import requests

# Отправка GET-запроса
response = requests.get('https://api.github.com')

if response.status_code == 200:
    print('Данные: ', response.json())
else:
    print('Ошибка при запросе: ', response.status_code)


### 2. Pandas


import pandas as pd  # Импортируем библиотеку pandas для работы с данными


# Функция для чтения данных из CSV файла
def read_data(file_path):
    """Читает данные из CSV файла и возвращает DataFrame."""
    try:
        data = pd.read_csv(file_path)  # Чтение данных из файла
        return data  # Возврат DataFrame
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")  # Если файл не найден
        return None
    except pd.errors.EmptyDataError:
        print("Файл пуст.")  # Если файл пуст
        return None
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")  # Обработка других ошибок
        return None


# Функция для анализа данных
def analyze_data(df):
    """Выполняет простой анализ данных и выводит результаты."""
    if df is not None:
        print("Первые 5 строк данных:")
        print(df.head())  # Вывод первых пяти строк DataFrame

        print("\nЗаголовки столбцов:")
        print(df.columns.tolist())  # Вывод заголовков столбцов

        print("\nСтатистическая информация:")
        print(df.describe(include='all'))  # Вывод статистической информации о данных

        # Подсчёт количества уникальных значений в каждом столбце
        print("\nКоличество уникальных значений в каждом столбце:")
        print(df.nunique())  # Возврат количества уникальных значений

        # Применение фильтрации для вывода данных, где зарплата больше 50000
        if 'Salary' in df.columns:
            filtered_df = df[df['Salary'] > 50000]  # Фильтрация данных
            print("\nОтфильтрованные данные (где Salary > 50000):")
            print(filtered_df)  # Вывод отфильтрованных данных
        else:
            print("Столбец 'Salary' не найден в данных.")  # Если столбец не найден

    else:
        print("Нет данных для анализа.")  # Если DataFrame пустой


# Пример использования функций
if __name__ == "__main__":
    file_path = "sample_data.csv"  # Путь к файлу CSV с данными

    # Чтение данных из CSV файла
    data = read_data(file_path)

    # Анализ данных
    analyze_data(data)


### 3. Matplotlib

import matplotlib.pyplot as plt

# Данные для построения графика
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Создание графика
plt.plot(x, y, marker='o')
plt.title('Простой график')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid()
plt.show()