import threading

def Even(No):
    for i in range(0, No + 1, 2):
        print("Even Thread:", i)

def Odd(No):
    for i in range(1, No + 1, 2):
        print("Odd Thread:", i)
        
def main():

    t1 = threading.Thread(target=Even, args=(20,))
    t2 = threading.Thread(target=Odd, args=(20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
