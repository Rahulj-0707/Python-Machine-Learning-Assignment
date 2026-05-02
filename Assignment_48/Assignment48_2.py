import numpy as np

def main():

    Arr = np.array([6, 7, 8, 9, 10, 11, 12])

    Sd = Arr.std()

    print("Standard Deviation is : ",Sd)

    Varience = Sd ** 2

    print("Varience is : ",Varience)
     
if __name__ == "__main__":
    main()

