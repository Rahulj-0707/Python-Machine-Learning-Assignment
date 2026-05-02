import os
import sys

def Compare(File1, File2):

    if not os.path.exists(File1):
        print("File1 does not exist.")
        return False

    if not os.path.exists(File2):
        print("File2 does not exist.")
        return False

    fobj1 = open(File1, "r")
    fobj2 = open(File2, "r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    fobj1.close()
    fobj2.close()

    if Data1 == Data2:
        return True
    else:
        return False


def main():

    if len(sys.argv) != 3:
        print("Invalid number of Arguments.")
        print("Please specify the name of files.")
        return

    Ret = Compare(sys.argv[1], sys.argv[2])

    if Ret == True:
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()
