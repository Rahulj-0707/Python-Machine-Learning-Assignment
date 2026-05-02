from functools import reduce

Maximum = lambda A,B : (A if A > B else B)

def main():
    Size = int(input("Enter the Number of elements:"))
    Value = 0

    Data = list()

    print("Enter the Elements : ")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    RData = reduce(Maximum, Data)
    print("Data after Reduce is : ", RData)

if __name__ == "__main__":
    main()