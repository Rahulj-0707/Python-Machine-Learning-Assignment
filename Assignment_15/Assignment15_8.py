Divisible = lambda No: ((No % 3 == 0) and (No % 5 == 0))

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    fData = list(filter(Divisible, Data))
    print("Data after filter is : ", fData)

if __name__ == "__main__":
    main()