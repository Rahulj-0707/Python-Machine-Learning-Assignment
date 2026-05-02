import os
import sys

def CopyData(Source, Destination):
    if not os.path.exists(Source):
        print("There is no such file : ")
        return
    
    fobj1 = open(Source,"r")
    fobj2 = open(Destination, "w")

    Data = fobj1.read()
    fobj2.write(Data)

    fobj1.close()
    fobj2.close()

    print(f"Data from {Source} to {Destination} copied successfully : ")

def main():
    if(len(sys.argv) != 3):
        print("Invalid number of Arguments : ")
        print("Plese specify the name of files : ")
        return

    CopyData((sys.argv[1]),(sys.argv[2]))

if __name__ == "__main__":
    main()