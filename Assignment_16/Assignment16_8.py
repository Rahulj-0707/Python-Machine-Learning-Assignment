def Pattern(No):
    for i in range(1,No+1,1):
        print(" * ")
    
def main():

    Value = int(input("Enter a number : "))
    Pattern(Value)
    
if __name__ == "__main__":
    main()