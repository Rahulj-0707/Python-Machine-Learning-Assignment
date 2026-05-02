import os
import sys

def CountWords(FileName):

    if not os.path.exists(FileName):
        print("There is no such a file : ")
        return
    
    fobj = open(FileName)
    Data = fobj.read()

    fobj.close()

    Words = Data.split()
    Count = len(Words)

    return Count 

def main():
    if len(sys.argv) != 2:
        print("Invalid Number of Arguments")
        print("Please specify the name of file")
        return 

    Ret = CountWords(sys.argv[1])
    print("Number of words in the file is : ",Ret)

if __name__ == "__main__":
    main()