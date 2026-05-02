Even = lambda iNo : True if iNo % 2 == 0 else False

def main():
    Value = int(input("Enter a number : "))
    Ret = Even(Value)
    print(Ret)

if __name__ == "__main__":
    main()
