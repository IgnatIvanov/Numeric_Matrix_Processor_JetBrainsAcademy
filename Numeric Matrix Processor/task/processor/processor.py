answer = []

dimmensions1 = input().split(' ')
matrix1 = []
for row in range(int(dimmensions1[0])):
    matrix1.append([int(x) for x in input().split(' ')])

dimmensions2 = input().split(' ')
matrix2 = []
for row in range(int(dimmensions2[0])):
    matrix2.append([int(x) for x in input().split(' ')])

if dimmensions2 != dimmensions1:
    print('ERROR')
else:
    for row in range(int(dimmensions1[0])):
        answer.append([matrix1[row][column] + matrix2[row][column] for column in range(int(dimmensions1[1]))])
        print(*answer[row])