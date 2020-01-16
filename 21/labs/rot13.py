"""
 This is the loop program over string
 Henry Lei
 Spring 2020
"""


def rot13():
    text = input("Enter text to encrypt: ")

    # prepare a regular alphabet
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # prepare a encrypted-order alphabet
    encrypted = "nopqrstuvwxyzabcdefghijklm"
    output = ""
    # parse each character in the input text
    for c in text:
        # find the position in the regular alphabet
        index = alphabet.find(c)
        if index < 0:
            # if not found, use the plain text
            output = output + c
        else:
            # if found, replace the character with the corresponding encrypted character - sharing the same index
            output = output + encrypted[index]
            # accumulator pattern is used

    print(output)


def rot13_v2():
    text = input("Enter text to encrypt: ")
    output = ""
    for c in text.lower():
        # from a to m
        if (ord(c) > 96) and (ord(c) < 110):
            output += chr(ord(c) + 13)
        # from n to z
        elif (ord(c) >= 110) and (ord(c) < 123):
            output += chr(ord(c) - 13)
        else:
            output += c

    print(output)


rot13_v2()
