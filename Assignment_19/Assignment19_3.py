from functools import reduce 

Greater = lambda No : No >= 70 and No <= 90 
Increament = lambda No : No + 10
Product = lambda A,B: A * B


def main():
    Size = int(input("Enter number of elments : "))

    Data = list()

    for i in range(Size):
        Value = int(input())

        Data.append(Value)
    
    print(Data)

    FData = list(filter(Greater, Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increament, FData))
    print("Data after map is : ",MData)

    RData = reduce(Product, MData)
    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()

