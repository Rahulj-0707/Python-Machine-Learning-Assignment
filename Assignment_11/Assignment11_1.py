def Area(No1, No2):
    Area = No1 * No2

    return Area

def main():
    Length = int(input("Enter the length of the rectangle: "))
    Width = int(input("Enter the width of the rectangle: "))

    Ret = Area(Length,Width)
    print("Area of rectangle is :",Ret)

if __name__ == "__main__":
    main()
