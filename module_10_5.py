import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    # Линейный вызов
    start_time = time.perf_counter()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.perf_counter() - start_time
    print(f'{linear_duration} (линейный)')

    # Многопроцессный вызов
    start_time = time.perf_counter()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multi_duration = time.perf_counter() - start_time
    print(f'{multi_duration} (многопроцессный)')
