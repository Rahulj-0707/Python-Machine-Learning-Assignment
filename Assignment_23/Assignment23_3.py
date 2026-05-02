class Number:

    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2,self.Value):
            if(self.Value % i == 0):
                return False
        return True
    
    def ChkPerfect(self):
        Sum = 0
        for i in range(1, self.Value):
            if(self.Value % i == 0):
                Sum = Sum + i
        
        if(Sum == self.Value):
            return True
        
        else:
            return False
        
    def Factors(self):
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                print(i)

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum = Sum + i
        
        return Sum
        
def main():

    Ret = False

    obj = Number(20)
    Ret = obj.ChkPrime()
    if(Ret == True):
        print("It is Prime Number : ")
    else:
        print("It is not an Prime Number : ")
    
    Ret = obj.ChkPerfect()
    if(Ret == True):
        print("It is a Perfect Number : ")
    else:
        print("It is not an Perfect Number : ")

    obj.Factors()

    Result = obj.SumFactors()
    print("Sum of Factors is : ", Result)


if __name__ == "__main__":
    main()