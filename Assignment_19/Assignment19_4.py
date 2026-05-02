from functools import reduce 

Even = lambda No : No % 2 == 0
Square = lambda No : No**2
Sum = lambda A,B : A + B

def main():
    Size = int(input("Enter number of elments : "))

    Data = list()

    for i in range(Size):
        Value = int(input())

        Data.append(Value)
    
    print(Data)

    FData = list(filter(Even, Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square, FData))
    print("Data after map is : ",MData)

    RData = reduce(Sum, MData)
    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()

