class Demo:
    Value = 0 

    def __init__(self, A, B):
        self.no1 = A
        self.no2 = B

    def fun(self):
        print("Inside fun method")
        print("Value of no1", self.no1)
        print("Value of no2", self.no2)

    def gun(self):
        print("Inside gun method")
        print("Value of no1", self.no1)
        print("Value of no2", self.no2)
        
def main():

    obj1 = Demo(11, 21)
    obj2 = Demo(51, 101)

    obj1.fun()
    obj2.gun()

    obj1.fun()
    obj2.gun()

if __name__ == "__main__":
    main()
