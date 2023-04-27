N = int(input("데이터 입력: ")) # N정수
numbers = list(map(int, input("테스트 수열 입력: ").split()))
LQ = []
RQ = []
MS = []
for i in range(N):
    RQ.append(i+1)
    
i = 0
while True:
    if RQ[0] == numbers[i]:
        e = RQ[0]
        RQ.pop(0)
        LQ.append(e)
        i += 1
    elif RQ[0] > numbers[i]:
        if MS[-1] == numbers[i]:
            e = MS[-1]
            MS.pop(-1)
            LQ.append(e)
            i += 1
        else:
            break            
    else:
        e = RQ[0]
        RQ.pop(0)
        MS.append(e)
        
    if i == N:
        break          
print(numbers)   
print(LQ)
print(MS)
if len(RQ) == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")


        

    


