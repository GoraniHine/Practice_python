N, K = map(int, input("총사람수와 순서를 입력하시오: ").split()) #사람수와 빠질순서

Q = []

for i in range(N): #큐에 숫자 삽입
    Q.append(i+1)
    
for i in range(N):
    counter = 0
    for j in range(K):
        e = Q[0]
        Q.pop(0)
        
        if len(Q) == 0:
            print("살아남은 번호: %d" %e)
            break
        
        counter += 1 # 1번째부터 시작하여 
        if counter == K: # K번째일때 풍덩
            print(e, end=" ")
        else: #아닐경우 다시 enqueue
            Q.append(e)    
        
        
        
