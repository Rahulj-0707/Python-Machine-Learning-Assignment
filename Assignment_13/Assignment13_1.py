def Divisible(Ch):
    if Ch in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print("It is Vowel")
    else:
        print("It is not a Vowel")

def main():
    Value = input("Enter a Character: ")
    Divisible(Value)

if __name__ == "__main__":
    main()
