def Factor(No):
    Count = 0
    for i in range(1,No):
        if (No % i == 0):
            Count = Count + i
    return Count


def main():
    Value = int(input("Enter a number : "))
    Ret = Factor(Value)
    print("Sum of all factors : ",Ret)

if __name__ == "__main__":
    main()