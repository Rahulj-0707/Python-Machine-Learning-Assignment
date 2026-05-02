from functools import reduce

Product = lambda A,B : A*B

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    fData = reduce(Product, Data)
    print("Data after filter is : ", fData)

if __name__ == "__main__":
    main()