import os
import sys

def DisplayLines(FileName):

    if not os.path.exists(FileName):
        print("There is no such a file : ")
        return
    
    fobj = open(FileName,"r")

    for i in fobj:
        print(i)
    
    fobj.close

def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments")
        print("Please specify the name of file")
        return 

    DisplayLines(sys.argv[1])

if __name__ == "__main__":
    main()