import threading

def SumEven(List,Length):
    Sum = 0
    for i in range(Length):
        if(List[i] % 2 == 0):
            Sum = Sum + List[i]
    print("Sum of all Even elements are : ", Sum)

def SumOdd(List,Length):
    Sum = 0
    for i in range(Length):
        if(List[i] % 2 != 0):
            Sum = Sum + List[i]
    print("Sum of all Odd elements are : ", Sum)

      
def main():

    Size = int(input("Enter the number of elements : "))

    Data = list()
    for i in range(Size):
        Value = int(input())
        Data.append(Value)
    
    print(Data)

    t1 = threading.Thread(target=SumEven, args=(Data,Size,))
    t2 = threading.Thread(target=SumOdd, args=(Data,Size,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()