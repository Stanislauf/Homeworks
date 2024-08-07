import random
def get_cipher():
    numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    numbers_choi = list(range(3, 21))
    cipher = random.choice(numbers_choi)
    return cipher

def get_passcode():
    passdict = {3: 12, 4: 13, 5: 1423, 6: 121524, 7: 162534, 8: 13172635, 9: 1218273645,
    10: 141923283746, 11: 11029384756, 12: 12131511124210394857, 13: 112211310495867,
    14: 1611325212343114105968, 15: 1214114232133124115106978,
    16: 1317115262143531341251161079, 17: 11621531441351261171089,
    18: 12151811724272163631545414513612711810, 19: 118217316415514613712811910,
    20: 13141911923282183731746416515614713812911}
    passcode = passdict.get(num)
    return passcode

num = get_cipher()
print('Шифр: ', num)

num_list = []
result = []
result2 = []
k = 1
while k <= num:
    num_list.append(k)
    k = k + 1
# print(num_list)

for i in num_list:
    if i < num / 2:
        for j in range(2, len(num_list) + 1):
            if j == i or j < i:
                continue
            if num % (i + j) == 0:
                result.append([i, j])
                result2.append(i)
                result2.append(j)

    else:
        break
print('Пары чисел: ', *result)
result2 = ''.join(map(str, result2))
result2 = result2.replace(' ', '')
result2 = int(result2)
print("Введите пароль: ", result2)

if int(result2) == get_passcode():
    print('Пароль подходит!', get_passcode())