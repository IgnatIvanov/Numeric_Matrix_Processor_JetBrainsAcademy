def matrixmult(m1, m2):
    s = 0     # сумма
    t = []    # временная матрица
    m3 = []  # конечная матрица
    if len(m2) != len(m1[0]):
        print("Матрицы не могут быть перемножены")
    else:
        r1 = len(m1)  # количество строк в первой матрице
        c1 = len(m1[0])  # Количество столбцов в 1
        r2 = c1           # и строк во 2ой матрице
        c2 = len(m2[0])  # количество столбцов во 2ой матрице
        for z in range(0, r1):
            for j in range(0, c2):
                for i in range(0, c1):
                    s = s + m1[z][i] * m2[i][j]
                t.append(s)
                s = 0
            m3.append(t)
            t = []
    return m3

def det(matrix):
    if len(matrix) == 0:
        return 0
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if len(matrix) > 2:
        answer = 0

        for i in range(len(matrix)):
            a_matrix = []
            for x in range(len(matrix)):
                T = []
                for y in range(len(matrix)):
                    T.append(matrix[x][y])
                a_matrix.append(T)
            del a_matrix[i]
            for j in range(len(a_matrix)):
                del a_matrix[j][0]
            answer += det(a_matrix) * pow(-1, 0 + i) * matrix[i][0]
        return answer

option = 100
while option != 0:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit""")
    option = int(input("Your choice: "))

    if option == 1:
        answer = []

        dimmensions1 = input("Enter size of first matrix: ").split(' ')
        matrix1 = []
        print("Enter first matrix: ")
        for row in range(int(dimmensions1[0])):
            matrix1.append([float(x) for x in input().split(' ')])

        dimmensions2 = input("Enter size of second matrix: ").split(' ')
        matrix2 = []
        print("Enter second matrix: ")
        for row in range(int(dimmensions2[0])):
            matrix2.append([float(x) for x in input().split(' ')])

        if dimmensions2 != dimmensions1:
            print('The operation cannot be performed.')
        else:
            print("The result is:")
            for row in range(int(dimmensions1[0])):
                answer.append([matrix1[row][column] + matrix2[row][column] for column in range(int(dimmensions1[1]))])
                print(*answer[row])
    elif option == 2:
        dimm = input("Enter size of matrix: ").split(' ')

        matrix = []
        print("Enter matrix:")
        for row in range(int(dimm[0])):
            matrix.append([float(x) for x in input().split(' ')])
        m = float(input("Enter constant: "))
        answer = []
        print("The result is:")
        for row in range(int(dimm[0])):
            answer.append([matrix[row][column] * m for column in range(int(dimm[1]))])
            print(*answer[row])
    elif option == 3:
        dimm1 = input("Enter size of first matrix: ").split(' ')
        matrix1 = []
        print("Enter first matrix: ")
        for row in range(int(dimm1[0])):
            matrix1.append([float(x) for x in input().split(' ')])

        dimm2 = input("Enter size of second matrix: ").split(' ')
        matrix2 = []
        print("Enter second matrix: ")
        for row in range(int(dimm2[0])):
            matrix2.append([float(x) for x in input().split(' ')])

        if int(dimm1[1]) != int(dimm2[0]):
            print('The operation cannot be performed.')
        else:
            answer = []
            answer = matrixmult(matrix1, matrix2)

            print("The result is:")
            for row in range(int(dimm1[0])):
                print(*answer[row])
    elif option == 4:
        print("""
1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line""")
        choice = int(input("Your choice: "))

        dimm = input("Enter matrix size: ").split(' ')
        matrix = []
        answer = []
        print("Enter matrix: ")
        for row in range(int(dimm[0])):
            in_str = input().split(' ')
            matrix.append([x for x in in_str])
            answer.append([x for x in in_str])

        if choice == 1:
            for row in range(int(dimm[0])):
                for column in range(int(dimm[1])):
                    answer[row][column] = matrix[column][row]

            print("The result is:")
            for row in range(int(dimm[0])):
                print(*answer[row])
        elif choice == 2:
            for row in range(int(dimm[0])):  # Main diagonal
                for column in range(int(dimm[1])):
                    answer[row][column] = matrix[column][row]

            for row in range(int(dimm[0])):  # Saving
                for column in range(int(dimm[1])):
                    matrix[row][column] = answer[row][column]

            for row in range(int(dimm[0])):  # Inverting
                for column in range(int(dimm[1])):
                    answer[row][column] = matrix[int(dimm[0])-1-row][int(dimm[1])-1-column]

            print("The result is:")
            for row in range(int(dimm[0])):
                print(*answer[row])
        elif choice == 3:
            for row in range(int(dimm[0])):  # Inverting
                for column in range(int(dimm[1])):
                    answer[row][column] = matrix[row][int(dimm[1])-1-column]

            print("The result is:")
            for row in range(int(dimm[0])):
                print(*answer[row])
        elif choice == 4:
            for row in range(int(dimm[0])):  # Inverting
                for column in range(int(dimm[1])):
                    answer[row][column] = matrix[int(dimm[0])-1-row][column]

            print("The result is:")
            for row in range(int(dimm[0])):
                print(*answer[row])
    elif option == 5:
        dimm = input("Enter matrix size: ").split(' ')
        m = []
        print("Enter matrix: ")
        for row in range(int(dimm[0])):
            in_str = input().split(' ')
            m.append([float(x) for x in in_str])

        print(det(m))
    elif option == 6:
        dimm = input("Enter matrix size: ").split(' ')
        m = []
        print("Enter matrix: ")
        for row in range(int(dimm[0])):
            in_str = input().split(' ')
            m.append([float(x) for x in in_str])

        answer = []
        cofactors_m = []
        transposed_cofactors_m = []
        for x in range(len(m)):
            T = []
            for y in range(len(m)):
                T.append(0)
            cofactors_m.append(T)

        det_m = det(m)
        if det_m == 0:
            print("This matrix doesn't have an inverse.")
        else:
            for column in range(len(m)):
                for row in range(len(m)):
                    minor_matrix = []
                    for x in range(len(m)):
                        T = []
                        for y in range(len(m)):
                            T.append(m[x][y])
                        minor_matrix.append(T)
                    del minor_matrix[column]
                    for j in range(len(minor_matrix)):
                        del minor_matrix[j][row]
                    cofactors_m[column][row] = det(minor_matrix) * pow(-1, column + row)

            for row in range(len(m)):
                T = []
                for column in range(len(m)):
                    T.append(cofactors_m[column][row])
                transposed_cofactors_m.append(T)

            for row in range(int(dimm[0])):
                answer.append([transposed_cofactors_m[row][column] / det_m for column in range(len(m))])
                print(*answer[row])