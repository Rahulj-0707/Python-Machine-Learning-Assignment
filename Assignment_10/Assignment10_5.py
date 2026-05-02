def OddNumber(No):
    for i in range(1,No+1,1):
        if(i % 2 != 0):
            print(i)
    
def main():
    Value = int(input("Enter a Number:"))
    OddNumber(Value)
    
if __name__ == "__main__":
    main()