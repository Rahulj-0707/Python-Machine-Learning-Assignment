def Cube(No):
    Result = No ** 3
    return Result
    
def main():
    Value = int(input("Enter number:"))
    Ret = Cube(Value)
    print("Cube of a number is:", Ret)
    

if __name__ == "__main__":
    main()