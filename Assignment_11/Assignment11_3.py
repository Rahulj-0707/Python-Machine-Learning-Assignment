def PerfectNumber(No):
    Count = 0
    for i in range(1, No):
        if(No % i == 0):
            Count = Count + i
    
    return Count

def main():
    Value = int(input("Enter a number:"))
    Ret = PerfectNumber(Value)

    if(Ret == Value):
        print("Number is perfect number:")
    else:
        print("Number is not an perfect number:")

if __name__ == "__main__":
    main()