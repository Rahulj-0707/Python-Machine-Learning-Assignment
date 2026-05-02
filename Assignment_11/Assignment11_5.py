def Grade(No):
    if No > 100 or No < 0:
        print("Invalid Marks")

    elif No >= 75:
        print("Distinction")
    
    elif No >= 60:
        print("First Class")

    elif No >= 50:
        print("Second Class")
    
    else:
        print("Fail")

def main():
    Value = int(input("Enter marks: "))
    Grade(Value)
    
if __name__ == "__main__":
    main()
