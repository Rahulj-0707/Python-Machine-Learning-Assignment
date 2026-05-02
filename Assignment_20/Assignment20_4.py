import threading
def CountSmall(text):
    Count = 0
    for ch in text:
        if ch.islower():
            Count = Count + 1
    print("Lowercase characters :", Count)



def CountCapital(text):
    Count = 0
    for ch in text:
        if ch.isupper():
            Count = Count + 1
    print("Uppercase characters :", Count)


def CountDigit(text):
    Count = 0
    for ch in text:
        if ch.isdigit():
            Count =  Count + 1
    print("Digits :", Count)


def main():
    data = input("Enter a string: ")

    t1 = threading.Thread(target=CountSmall, args=data,)
    t2 = threading.Thread(target=CountCapital, args=data,)
    t3 = threading.Thread(target=CountDigit, args=data,)

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


if __name__ == "__main__":
    main()
