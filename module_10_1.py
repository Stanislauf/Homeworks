import time
from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1} \n')
            sleep(0.1)
    print(f'Завершилась запись файла {file_name}')

start_time = datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = datetime.now()
print(f"Время выполнения функций: {end_time - start_time}")

start_time = datetime.now()
thr_1 = Thread(target=write_words, args=(10, "example5.txt"))
thr_2 = Thread(target=write_words, args=(30, "example6.txt"))
thr_3 = Thread(target=write_words, args=(200, "example7.txt"))
thr_4 = Thread(target=write_words, args=(100, "example8.txt"))
thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()
thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
end_time = datetime.now()
print(f"Время выполнения функций: {end_time - start_time}")