def get_matrix(n, m , value):
    matrix = [[value]*m for _ in range(n)]
    for r in range(n): # Красивый табличный вывод матрицы
        for c in range(m):
            print(matrix[r][c], end=' ')
        print()
    return matrix # Вывод матрицы по заданию

print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))

