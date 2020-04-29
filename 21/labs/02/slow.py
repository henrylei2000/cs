"""
Slow Program
Henry Lei
Spring 2020
"""


def slow(length, text):
    output = ""
    for letter in text:
        output += letter + '.' * length
    return output


def main():
    # receive input
    length = int(input("Pause length: "))
    text = input("Text: ")

    # process input
    output = slow(length, text)

    # print output
    print(output)


if __name__ == "__main__":
    main()
