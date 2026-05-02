def Maximum(List, Length):

    Max = List[0]

    for i in range(Length):
        if(Max <= List[i]):
            Max = List[i]
    
    return Max


def main():

    Size = int(input("Enter the number of Elements : "))
    Data = list()

    for i in range(Size):
        Value = int(input())

        Data.append(Value)

    print(Data)

    Ret = Maximum(Data, Size)
    print("Maximum Element from the list is : ",Ret)

if __name__ == "__main__":
    main()