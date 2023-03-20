height = int(input('피라미드 높이?'))

for i in range(height):
    for k in range(height,i,-1):
        print(' ',end='')

    for k in range((i+1)*2-1):
        print("*",end='')
    print()
    
for i in range(1, height+1):
    print(" "*(height-i) + "*"*(2*i-1))