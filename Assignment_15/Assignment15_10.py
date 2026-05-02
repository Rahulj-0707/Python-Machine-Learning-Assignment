EvenCount = lambda No : (No % 2 == 0)

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    fData = list(filter(EvenCount, Data))
    print("Data after filter is : ", fData)

    print("Number of Even Element in the list is : ",len(fData))

if __name__ == "__main__":
    main()
