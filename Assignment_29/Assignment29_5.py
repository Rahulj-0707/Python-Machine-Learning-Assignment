import os
import sys

def StringCount(FileName, String):

    if not os.path.exists(FileName):
        print("There is no such file : ")
        return
    
    fobj = open(FileName, "r")
    Data = fobj.read()

    fobj.close()

    Count = Data.count(String)

    return Count

def main():

    if len(sys.argv) != 3:
        print("Invalid number of Arguments.")
        print("Please specify the name of files.")
        return

    Ret = StringCount(sys.argv[1], sys.argv[2])
    print("The count is : ",Ret)
    
if __name__ == "__main__":
    main()
