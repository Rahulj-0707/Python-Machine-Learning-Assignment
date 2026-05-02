Square = lambda No : (No**2)

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    MData = list(map(Square, Data))
    print("Data after map is : ", MData)

if __name__ == "__main__":
    main() 
