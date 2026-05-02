def SumElements(List,Length):
    Sum = 0
    for i in range(Length):
        Sum = Sum + List[i]

    return Sum



def main():
    Data = list()
    Size = int(input("Enter number of elements : "))
    
    
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print(Data)

    Ret = SumElements(Data, Size)
    print("Sum of all Elements is : ", Ret)


if __name__ == "__main__":
    main()
