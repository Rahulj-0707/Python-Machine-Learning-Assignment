def Frequency(List, Length, Find):

    Freq = 0
    for i in range(Length):
        if(Find == List[i]):
            Freq = Freq + 1
    
    return Freq


def main():

    Size = int(input("Enter the number of Elements : "))
    Data = list()

    for i in range(Size):
        Value = int(input())

        Data.append(Value)

    print(Data)

    Search = int(input("Enter the Number ot Search : "))

    Ret = Frequency(Data, Size, Search)
    print("Frequency of Element : ",Ret)

if __name__ == "__main__":
    main()