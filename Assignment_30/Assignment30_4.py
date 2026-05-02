import os 
import sys
import shutil

def CopyData(Source, Destination):
    if not os.path.exists(Source):
        print("There is no source file is present")
        return
    
    shutil.copy2(Source,Destination)
    print("Data copied successfully")
    
    
def main():

    if (len(sys.argv) != 3):
        print("Invalid Number of Arguments")
        print("Please specify the name of file")
        return

    CopyData(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()