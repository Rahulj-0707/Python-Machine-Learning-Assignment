import Arithmatic

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Arithmatic.Add(Value1, Value2)
    print("Addition is : ",Ret)

    Ret = Arithmatic.Sub(Value1, Value2)
    print("Substraction is : ",Ret)

    Ret = Arithmatic.Mult(Value1, Value2)
    print("Multiplication is : ",Ret)

    Ret = Arithmatic.Div(Value1, Value2)
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()
