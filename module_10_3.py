import threading
import random
import time


class Bank:
    def __init__(self):
        self.balance = 0  # Изначальный баланс банка
        self.lock = threading.Lock()  # Создаем объект замка

    def deposit(self):
        for _ in range(100):  # 100 транзакций пополнения
            amount = random.randint(50, 500)  # Случайное число от 50 до 500
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount
                print(f" Пополнение: {amount}. Баланс: {self.balance}")

                # Снимаем блокировку, когда это требуется
                if self.balance >= 500 and not self.lock.locked():
                    self.lock.release()

            time.sleep(0.001)  # Задержка для имитации скорости выполнения

    def take(self):
        for _ in range(100):  # 100 транзакций снятия
            amount = random.randint(50, 500)  # Случайное число от 50 до 500
            print(f"\nЗапрос на {amount}")

            with self.lock:  # Блокируем доступ к балансу
                # Если достаточно средств, производим снятие
                if amount <= self.balance:
                    self.balance -= amount
                    print(f" Снятие: {amount}. Баланс: {self.balance}")
                else:
                    # Если средств недостаточно, выводим сообщение
                    print("Запрос отклонён, недостаточно средств")
                    # Блокируем поток при недостатке средств
                    time.sleep(0.001)  # Имитация ожидания времени

            time.sleep(0.001)  # Задержка для имитации скорости выполнения


# Создание объекта класса Bank
bk = Bank()

# Создание 2 потоков для методов deposit и take
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

# Запуск потоков
th1.start()
th2.start()

# Ждем завершения обоих потоков
th1.join()
th2.join()

# Вывод окончательного баланса
print(f'Итоговый баланс: {bk.balance}')