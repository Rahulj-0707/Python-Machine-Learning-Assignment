def Area(Red,Pi):
    Area = Red * Pi 

    return Area

def main():
    Redius = int(input("Enter the redius of the circle: "))
    Pi = 3.14
    
    Ret = Area(Redius,Pi)
    print("Area of Circle is :",Ret)

if __name__ == "__main__":
    main()