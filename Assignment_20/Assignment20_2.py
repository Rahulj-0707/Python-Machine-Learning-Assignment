import threading

def SumEvenFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            Sum = Sum + i
    
    print("Sum of All even Factors : ", Sum)

def SumOddFactor(No):
    Sum = 0
    for i in range(1,No+1):
        if((No % i == 0) and (i % 2 != 0)):
            iSum = iSum + i
    
    print("Sum of All Odd Factors : ", Sum)

        
def main():

    Value = int(input("Enter a number : "))

    t1 = threading.Thread(target=SumEvenFactor, args=(Value,))
    t2 = threading.Thread(target=SumOddFactor, args=(Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()