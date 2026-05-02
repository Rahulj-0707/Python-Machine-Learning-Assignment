def PrimeNumber(No):
    for i in range(2, No):
        if(No % i == 0):
            return False
        else:
            return True

def main():
    Value = int(input("Enter a number : "))
    Ret = False
    Ret = PrimeNumber(Value)
    if Ret == True:
        print("It is Prime Number:")
    else:
        print("It is not an Prime Number:")


if __name__ == "__main__":
    main()
