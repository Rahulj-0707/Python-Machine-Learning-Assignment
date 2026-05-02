def Square(No):
    Squ = No ** 2
    return Squ
    
def main():
    Value = int(input("Enter number:"))
    Ret = Square(Value)
    print("Square of a number is:", Ret)
    

if __name__ == "__main__":
    main()