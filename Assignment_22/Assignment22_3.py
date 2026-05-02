class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))

    def Addition(self):
        Ans = self.Value1 + self.Value2
        return Ans

    def Substraction(self):
        Ans = self.Value1 - self.Value2
        return Ans
    
    def Multiplication(self):
        Ans = self.Value1 * self.Value2
        return Ans
    
    def Division(self):
        if self.Value2 == 0:
            print("We cannot divide by zero")
            return None
        else:
            Ans = self.Value1 / self.Value2
            return Ans


def main():

    obj1 = Arithmetic()
    obj1.Accept()

    Ret = obj1.Addition()
    print("Addition is : ", Ret)

    Ret = obj1.Substraction()
    print("Substraction is : ", Ret)

    Ret = obj1.Multiplication()
    print("Multiplication is : ", Ret)

    Ret = obj1.Division()
    print("Division is : ", Ret)

    print("-" * 50)

    obj2 = Arithmetic()
    obj2.Accept()

    Ret = obj2.Addition()
    print("Addition is : ", Ret)

    Ret = obj2.Substraction()
    print("Substraction is : ", Ret)

    Ret = obj2.Multiplication()
    print("Multiplication is : ", Ret)

    Ret = obj2.Division()
    print("Division is : ", Ret)


if __name__ == "__main__":
    main()