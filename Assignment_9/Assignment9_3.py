def Summation(No):
    Count = 0
    while(No != 0):
        Digit = No % 10
        Count = Count + Digit
        No = No // 10
    return Count
 

def main():
    Value = int(input("Enter a number : "))
    Ret = Summation(Value)
    print("Sum of all Digits ",Ret)

if __name__ == "__main__":
    main()