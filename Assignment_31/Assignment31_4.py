import os
import sys
import shutil

def CopyDirectory(Source, Destination, Ext):

    if not os.path.exists(Source):
        print("Thre is ni source file is present : ")
        return
    
    if not os.path.exists(Destination):
        os.mkdir(Destination)
        print("Destionation Directory is created Successfully : ")

    for FolderName, SubFolderName, FileName in os.walk(Source):
        for fname in FileName:
            if fname.endswith(Ext):
                SoucePath = os.path.join(Source, fname)
                DestPath = os.path.join(Destination, fname)

                if os.path.isfile(SoucePath):
                    shutil.copy2(SoucePath, DestPath)
            
    print(f"All files with {Ext} has copied successfully")

def main():

    if (len(sys.argv) != 4):
        print("Invalid number of argument\n")
        print("Plase enter the name of directory\n")
        return 

    CopyDirectory(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == "__main__":
    main()