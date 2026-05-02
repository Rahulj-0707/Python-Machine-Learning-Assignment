def SumDigit(No):
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10 
    return Sum
    
def main():
    Value = int(input("Enter a number : "))
    Ret = SumDigit(Value)
    print("Sum of all Digits :", Ret)

if __name__ == "__main__":
    main()