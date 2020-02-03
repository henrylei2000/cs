"""
Slow Program
Henry Lei
Spring 2020
"""

def simple_loop():
    length = int(input("Pause length: "))
    text = input("Text: ")

    for letter in text:
        print(letter)
        for i in range(length):
            print(".")


def loop():
    length = int(input("Pause length: "))
    text = input("Text: ")

    for letter in text:
        print(letter + '.' * length)


def slow():
    length = int(input("Pause length: "))
    text = input("Text: ")
    output = ""
    for letter in text:
        output += letter + '.' * length

    print(output)


def main():

    output = slow()
    print(output)


if __name__ == "__main__":
    main()
