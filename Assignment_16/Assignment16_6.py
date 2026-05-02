def Display(No):
    if(No == 0):
        print("Zero")

    elif(No < 0):
        print("Negative Number")

    else:
        print("Positive Number")
    

def main():

    Value = int(input("Enter a number : "))
    Display(Value)

if __name__ == "__main__":
    main()