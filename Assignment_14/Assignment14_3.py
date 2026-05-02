Maximum = lambda A,B : A if A > B else B

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Maximum(Value1, Value2)
    print("Maximum number is : ",Ret)

if __name__ == "__main__":
    main()
