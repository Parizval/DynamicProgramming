def factorial(n):
    if n == 0 or n == 1 : 
        return 1 
    else:
        return n*factorial(n-1)

class FactorialDynammic:
    
    def __init__(self):
        self.Table = {}
        self.Table[0] = 1 
        self.Table[1] = 1
    
    def  Solve(self,n):
        if n in  self.Table:
            return self.Table[n]
        
        self.Table[n-1] = self.Solve(n-1)

        Answer = n*self.Table[n-1]
        self.Table[n] = Answer
        
        return Answer

print(factorial(5))
Fact = FactorialDynammic()
# print(Fact.Table)
# print(Fact.Solve(5))
# print(Fact.Solve(1000))
while True:
    n = int(input("Enter Number:  "))
    if n == -1 :  
        break
    elif  n == -2 :  
        print(Fact.Table)
    else:
        print(Fact.Solve(n))
