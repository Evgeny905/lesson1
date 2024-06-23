def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append(i)
        for j in range(m):
            j = [value for _ in range(m)]
            matrix.append(j)

            return matrix




result1 = get_matrix(4,3,15)
print(result1)