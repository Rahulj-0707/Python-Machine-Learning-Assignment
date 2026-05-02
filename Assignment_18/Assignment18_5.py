import MarvellousNum

def main():

    Size = int(input("Enter the number of Elements : "))
    Data = list()

    for i in range(Size):
        iValue = int(input())

        Data.append(iValue)

    print(Data)

    Ret = MarvellousNum.ChkPrime(Data, Size)
    print("Sum of all Prime Numbers : ",Ret)

if __name__ == "__main__":
    main()