Even = lambda No : (No % 2 == 0)

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    FData = list(filter(Even, Data))
    print("Data after filter is : ", FData)

if __name__ == "__main__":
    main() 