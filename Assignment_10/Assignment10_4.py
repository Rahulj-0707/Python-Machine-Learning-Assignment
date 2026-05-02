def EvenNumber(No):
    for i in range(1,No+1,1):
        if(i % 2 == 0):
            print(i)
    
def main():
    Value = int(input("Enter a Number:"))
    EvenNumber(Value)
    
if __name__ == "__main__":
    main()