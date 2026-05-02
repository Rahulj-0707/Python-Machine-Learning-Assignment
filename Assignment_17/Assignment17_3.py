def Factorial(No):
    Count = 1
    for i in range(1,No+1):
        Count = Count * i
    return Count
    

def main():
    Value = int(input("Enter a number : "))
    Ret = Factorial(Value)
    print("Factorial is : ",Ret)

if __name__ == "__main__":
    main()