Largest = lambda A,B,C : A if (A > B and A > C) else (B if (B > C and B > A) else C)

def main():
    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))
    Value3 = int(input("Enter third number : "))


    Ret = Largest(Value1, Value2, Value3)
    print("Largest number is : ",Ret)

if __name__ == "__main__":
    main()
