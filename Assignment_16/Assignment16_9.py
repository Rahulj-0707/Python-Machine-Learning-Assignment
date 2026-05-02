def Even(No):
    for i in range(1,No+1,1):
        if(i % 2 == 0):
            print(i)
    
def main():
    Even(20)
    
if __name__ == "__main__":
    main()