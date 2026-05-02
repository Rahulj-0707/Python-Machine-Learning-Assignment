import os
import sys
import time

def DisplayDirectory(DirName, Ext1, Ext2):

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

    if not os.path.exists(DirName):
        print("There is such Directory present")
        return
    
    if not os.path.isdir(DirName):
        print("It is not an Directory")
        return
    
    for FolderName, SubFolderName, FileName in os.walk(DirName):
        for fname in FileName:
            fobj.write(fname+"\n")

            if fname.endswith(Ext1):
                OldPath = os.path.join(DirName, fname)

                NewFile = fname.replace(Ext1, Ext2)
                NewPath = os.path.join(DirName, NewFile)

                os.renames(OldPath, NewPath)
                fobj.write(f"Renamed {fname} to {NewFile}\n")
    
    fobj.write(Border+"\n")
    fobj.write("Renamed Successfully\n")
    fobj.write(Border+"\n")
    fobj.write("Thank you for using our script\n")
    fobj.write(Border+"\n")
    fobj.close()

def main():

    if (len(sys.argv) != 4):
        print("Invalid number of argument\n")
        print("Plase enter the name of directory\n")
        return 

    DisplayDirectory(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()