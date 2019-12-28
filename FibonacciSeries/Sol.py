class FibonacciSeries:

    def __init__(self):
        self.MemoryTable = {}
        self.MemoryTable[0] = 0 
        self.MemoryTable[1] = 1 

    def FibonacciMemory(self,n):

        if n in self.MemoryTable:
            return self.MemoryTable[n]

        self.MemoryTable[n-1] = self.FibonacciMemory(n-1)
        self.MemoryTable[n-2] = self.FibonacciMemory(n-2)

        Answer = self.MemoryTable[n-1] + self.MemoryTable[n-2]
        self.MemoryTable[n] = Answer
        return Answer

    def NaiveApproach(self,n):
        if n == 0 or n == 1 : return n 
        else : 
            return self.NaiveApproach(n-1) + self.NaiveApproach(n-2)

Fib = FibonacciSeries()
print(Fib.NaiveApproach(100))
