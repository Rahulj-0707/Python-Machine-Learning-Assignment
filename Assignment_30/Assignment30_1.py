import os
import sys

def LineCount(FileName):

    if not os.path.exists(FileName):
        print("There is no such a file : ")
        return
    
    fobj = open(FileName)
    Count = 0

    for i in fobj:
        Count = Count + 1
    
    fobj.close()

    return Count

def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments")
        print("Please specify the name of file")
        return 

    Ret = LineCount(sys.argv[1])
    print("Number of lines in the file is : ",Ret)

if __name__ == "__main__":
    main()
