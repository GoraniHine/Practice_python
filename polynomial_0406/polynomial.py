def Polynomial(deg): #모든 계수가 0인 deg차수의 다항식을 만든다.
    x = []
    for i in range(deg+1):
        x.append(0)
    return x
            
def readCoef(lst): #다항식의 차수별 계수를 입력받아 정한다.
    for i in range(len(lst)):
        lst[i] = int(input('이 다항식의 %d차 계수를 입력하시오: ' %i))
                
def degree(lst): #다항식의 차수를 반환한다.
    return len(lst)-1
        
def evaluate(lst, scalar): #미지수에 scalar를 넣어 계산한 결과를 반환한다.
    value = 0
    for i in range(len(lst)):
        value += lst[i]*scalar**i
    return value
        
def add(lst, rhs): #현재 다항식과 다항식 rhs를 더한 새로운 다항식을 만들어 반환한다.
    stack1, stack2 = 0, 0
    Y =[]
    while True:
        if len(lst) == len(rhs):
            break
        elif len(lst) < len(rhs):
            for x in range(len(lst), len(rhs), 1):
                lst.append(0)
                stack1 += 1                                    
        elif len(lst) > len(rhs):
            for y in range(len(rhs), len(lst), 1):
                rhs.append(0)
                stack2 += 1
    for i in range(len(lst)):
        Y.append(0)
        Y[i] = lst[i] + rhs[i]
    if stack1 > 0:
        for a in range(stack1):
            lst.pop(-1)
    elif stack2 >0:
        for b in range(stack2):
            rhs.pop(-1)
    return Y

def sub(lst, rhs): #현재 다항식과 다항식 rhs를 뺀 새로운 다항식을 만들어 반환한다.
    stack1, stack2 = 0, 0
    Y =[]
    while True:
        if len(lst) == len(rhs):
            break
        elif len(lst) < len(rhs):
            for x in range(len(lst), len(rhs), 1):
                lst.append(0)
                stack1 += 1                                    
        elif len(lst) > len(rhs):
            for y in range(len(rhs), len(lst), 1):
                rhs.append(0)
                stack2 += 1
    for i in range(len(lst)):
        Y.append(0)
        Y[i] = lst[i] - rhs[i]
    if stack1 > 0:
        for a in range(stack1):
            lst.pop(-1)
    elif stack2 >0:
        for b in range(stack2):
            rhs.pop(-1)
    return Y
        
def multiply(lst, rhs): #현재 다항식과 다항식 rhs를 곱한 새로운 다항식을 만들어 반환한다.
    result = []
    for i in range(len(lst)+len(rhs)-1):
        result.append(0)
    for i in range(len(lst)):
        for j in range(len(rhs)):
            result[i+j] += lst[i] * rhs[j]
    return result
            
def display(lst, string): #현재 다항식을 화면에 str 뒤에 출력한다.
    degree = len(lst) - 1
    output = ""
    
    for i in range(len(lst)-1, -1 , -1):
        if lst[i] != 0:
            if degree == 0:
                output += str(lst[i])
            elif degree == 1:
                output += f"{lst[i]}x + "
            else:
                output += f"{lst[i]}x^{degree} + "
        
        degree -= 1
    print(string, output)
   
a = Polynomial(2)
b = Polynomial(1)
readCoef(a)
readCoef(b)
print(a)
print(b)        
print('a 다항식의 차수는 :', degree(a))
print('b 다항식의 차수는 :', degree(b))
c = add(a, b)
d = sub(a, b)
print(c)
print(d)
print(evaluate(c, 2)) 
print(evaluate(d, 2)) 
e = multiply(a, b) 
print(e)
display(e, 'e 다항식은: ')