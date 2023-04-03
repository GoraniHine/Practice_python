height = int(input('높이를 입력하시오: '))

mat = [['-' for j in range(2**height)] for i in range(height)]

def drawTree(row, left, right):
    mid = (left + right) // 2
    if row == 0:
        mat[row][mid] = 'X'
        return
    mat[row][mid] = 'X'
    drawTree(row-1, left, mid-1)
    drawTree(row-1, mid+1, right)

drawTree(height-1, 0, 2**height)

mat = list(reversed(mat))

for i in mat:
    print("".join(str(j) for j in i))