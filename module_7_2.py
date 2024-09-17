from pprint import pprint
import io
def custom_write(file_name, strings):
    str_pos = {}
    file = open(file_name, 'w', encoding='utf-8')
    for i, str in enumerate(strings, start=1):
        byte_pos = file.tell()
        file.write(f'{str}\n')
        str_pos[(i, byte_pos)] = str
    file.close()
    return str_pos


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)