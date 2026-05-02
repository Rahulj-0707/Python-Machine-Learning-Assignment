import threading

def ForwordLoop(No):
    for i in range(No+1):
        print(i)

def ReverceLoop(No):
    for i in range(No+1,1,-1):
        print(i)
      
def main():

    t1 = threading.Thread(target=ForwordLoop, args=(50,))
    t2 = threading.Thread(target=ReverceLoop, args=(50,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()