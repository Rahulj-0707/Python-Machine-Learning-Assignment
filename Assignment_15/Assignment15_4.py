from functools import reduce

Addition = lambda A,B : (A + B)

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    RData = reduce(Addition, Data)
    print("Data after Reduce is : ", RData)

if __name__ == "__main__":
    main()