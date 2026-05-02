import os 
import sys

def ChkWord(FileName, Word):
    if not os.path.exists(FileName):
        print("There is no such file is present")
        return
    
    fobj = open(FileName, "r")
    Data = fobj.read()

    Words = Data.split()

    for i in Words:
        if(Word == i):
            fobj.close()
            return True
        
    fobj.close()
    return False
           

def main():
    if(len(sys.argv) != 3):
        print("Invalid Number of Arguments")
        print("Plese specify the name of the file")
        return
    
    Ret = ChkWord(sys.argv[1], sys.argv[2])
    if(Ret == True):
        print("The word is present in the file")
    else:
        print("The word is not present in the file")

if __name__ == "__main__":
    main()