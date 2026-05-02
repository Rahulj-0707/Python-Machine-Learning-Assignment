from functools import reduce 

PrimeNumber = lambda No : No > 1 and all(No % i != 0 for i in range(2, No))
Multiply = lambda No : No * 2
Maximum = lambda A, B : A if A >= B else B

def main():
    Size = int(input("Enter number of elments : "))

    Data = list()

    for i in range(Size):
        Value = int(input())

        Data.append(Value)
    
    print(Data)

    FData = list(filter(PrimeNumber, Data))
    print("Data after filter is : ",FData)

    MData = list(map(Multiply, FData))
    print("Data after map is : ",MData)

    RData = reduce(Maximum, MData)
    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()

