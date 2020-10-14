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

option = 100
while option != 0:
    print("""1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
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
            #row = []
            #for i in range(int(dimm1[0])):
            #    row.append(0)
            #for i in range(int(dimm2[1])):
            #    answer.append(row)

            #for row in range(int(dimm1[0])):
            #    for column in range(int(dimm2[1])):


            #        answer[row][column] = +
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