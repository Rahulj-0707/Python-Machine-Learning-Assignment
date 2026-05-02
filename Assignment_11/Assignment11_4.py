def BinaryEquivalent(No):
    Num = 0
    while(No != 0):
        Digit = No % 2
        print(Digit)
        No = No // 2

def main():
    Value = int(input("Enter a number:"))
    BinaryEquivalent(Value)
    
if __name__ == "__main__":
    main()