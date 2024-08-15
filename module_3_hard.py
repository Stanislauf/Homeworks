data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

sum_int = 0
sum_str = 0

def calc_all(data):
  global sum_int, sum_str
  if isinstance(data, dict):
    for key in data.keys():
      calc_all(key)
    for value in data.values():
      calc_all(value)
  elif isinstance(data, tuple) or isinstance(data, set) or isinstance(data, list):
    for item in data:
      calc_all(item)
  elif isinstance(data, int):
    sum_int = sum_int + data
  elif isinstance(data, str):
    sum_int = sum_int + len(data)
  return sum_int + sum_str

print(f'Сумма числовых значений и сумма строковых значений равна: ', calc_all(data_structure))