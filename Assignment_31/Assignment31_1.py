import os
import sys
import time

def DisplayDirectory(DirName = "Marvellous"):

    Border = "_" * 50

    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj = open(LogFileName,"w")

    fobj.write(Border+"\n")
    fobj.write("This is a file created by Marvellous Automation\n")
    fobj.write("This is a Directory Display Script\n")
    fobj.write(Border+"\n")

    Ret = False

    Ret = os.path.exists(DirName)
    if(Ret == False):
        print("There is no such directory exist ")
    
    Ret = os.path.isdir(DirName)
    if(Ret == False):
        print("It is not an directory")

    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fobj.write(fname+"\n")

    fobj.write(Border+"\n")
    fobj.write("Thank you for using our script\n")
    fobj.write(Border+"\n")
    fobj.close()

def main():

    if (len(sys.argv) != 2):
        print("Invalid number of argument\n")
        print("Plase enter the name of directory\n")
        return 

    DisplayDirectory(sys.argv[1])

if __name__ == "__main__":
    main()
