def CountDigit(No):
    Count = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Count = Count + 1
        No = No // 10 
    return Count
    
def main():
    Value = int(input("Enter a number : "))
    Ret = CountDigit(Value)
    print("Number of Digits are:", Ret)

if __name__ == "__main__":
    main()