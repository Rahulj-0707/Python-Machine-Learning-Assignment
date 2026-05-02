def String(str):
    Count = 0
    Count = len(str)
    return Count
    
def main():

    Value = input("Enter a word : ")
    Ret = String(Value)
    print("Number of Character in the word is : ",Ret)
    
if __name__ == "__main__":
    main()