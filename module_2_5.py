def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix

n = int(input('Введите длину строки:  '))
m = int(input('ВВедите количество столбцов:  '))
value = input('ВВедите значение матрицы:  ')
matrix = get_matrix(n, m, value)














#'''matrix_str = []
#n = 3
#m = 4
#volume = 5
#for i in range(n):
#    matrix_str.append(volume) # n длина строки m размер столбцов volume значение
#    if i == n:
#        break
#for j in range(m):
#    matrix.append(matrix_str) # n длина строки m размер столбцов volume значение
#    if j == m:
#        break
#print(matrix)'''