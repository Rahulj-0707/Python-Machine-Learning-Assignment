String = lambda s: len(s) > 5

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = input()
        Data.append(Value)

    print(Data)

    fData = list(filter(String, Data))
    print("Data after filter is : ", fData)

if __name__ == "__main__":
    main()