import sys
import os 

def Display(Dirname = "Marvellous"):
    Ret = False

    Ret = os.path.exists(Dirname)
    if(Ret == False):
        print("There is no such a file exist : ")
    else:
        print("The file is present in the storage : ")
    
    fobj = open(Dirname, "r")
    Data = fobj.read()
    print(Data)
    fobj.close()
        
def main():
    if(len(sys.argv) != 2):
        print("Invaklid number of arguments : ")
        print("Please specify the name of directory : ")
        return
    
    Display(sys.argv[1])

if __name__ == "__main__":
    main()
    