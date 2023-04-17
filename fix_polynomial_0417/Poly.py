class Poly:
    def __init__(self, degree = 0):
        self.degree = degree
        self.coef = [0 for _ in range(degree + 1)]
    
    def readcoef(self, coefs):
        for item in coefs:
            exp, coef = item
            self.coef[exp] = coef

    def add(self, rhs):
        newPoly = Poly(max(self.degree, rhs.degree))
        if (self.degree <= rhs.degree ):
            for i in range(self.degree + 1):
                newPoly.coef[i] = self.coef[i] + rhs.coef[i]
            for i in range(self.degree + 1, rhs.degree + 1):
                newPoly.coef[i] = rhs.coef[i]
        else:
            for i in range(rhs.degree + 1):
                newPoly.coef[i] = self.coef[i] + rhs.coef[i]
            for i in range(rhs.degree + 1, self.degree + 1):
                newPoly.coef[i] = self.coef[i]
        return newPoly

    def mul(self, rhs):
        newPoly = Poly(self.degree + rhs.degree)

        for i in range(self.degree + 1):
            for j in range(rhs.degree + 1):
                coef = self.coef[i] * rhs.coef[j]
                newPoly.coef[i + j] = coef
        return newPoly
    def display(self, name):
        print(name, '=', end = ' ', sep = '')
        for i in range(self.degree, 0 , -1):
            print(self.coef[i], 'x^', i, ' + ', end = '', sep = '')
        print(self.coef[0], 'x^0', sep = '')
        print()

A = Poly(2)
A.readcoef([(2, 5), (1, -3), (0, 12)])
A.display('A(X) ')
B = Poly(3)
B.readcoef([(3, 2), (2, -6), (0, -4)])
B.display('B(X) ')

C = A.add(B)
C.display('C(X) ')
D = A.mul(B)
D.display('D(X) ')