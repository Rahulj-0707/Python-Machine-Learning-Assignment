def Divisible(No):
    if(No % 5 == 0 and No % 3 == 0):
        print("The number is divisible by 5 and 3")
    
def main():
    Value = int(input("Enter number:"))
    Divisible(Value)
    
if __name__ == "__main__":
    main()