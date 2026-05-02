import sys
import os
import hashlib
import time

def CheckSum(DirName):

    Border = "_" * 50

    timestamp = time.ctime()

    LogFileName = "Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    lobj = open(LogFileName,"w")

    lobj.write(Border+"\n")
    lobj.write("This is a file created by Rahuls Automation\n")
    lobj.write("This is a Directory Display Script\n")
    lobj.write(Border+"\n")

    if not os.path.exists(DirName):
        lobj.write("There is no such directory\n")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:

            path = os.path.join(FolderName, fname)

            fobj = open(path, "rb")

            hobj = hashlib.md5()

            Buffer = fobj.read(1024)

            while len(Buffer) > 0:
                hobj.update(Buffer)
                Buffer = fobj.read(1024)
            
            fobj.close()

            lobj.write(f"{path} : {hobj.hexdigest()}\n")

    lobj.write(Border+"\n")
    lobj.write("Thank you for using our script\n")
    lobj.write(Border+"\n")
    lobj.close()

def main():
    if len(sys.argv) != 2:
        print("Invalid number of arguments")
        print("Please specify the name of directory")
        return
    
    CheckSum(sys.argv[1])
    
if __name__ == "__main__":
    main()
