def SumNumber(No):
    Count = 0
    for i in range(1,No+1,1):
        Count = Count + i

    return Count
    
def main():
    Value = int(input("Enter a Number:"))
    Ret = SumNumber(Value)
    print("Sum of First N natural numbers:", Ret)
    
if __name__ == "__main__":
    main()