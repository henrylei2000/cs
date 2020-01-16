"""
 This is the loop program over string
 Henry Lei
 Spring 2020
"""


def ladder():
    text = input("Enter some text: ")
    size = len(text)
    for i in range(size):
        print("%s--%s" % (text[i], text[size - i - 1]))


def star_box():
    size = int(input("Enter box size: "))
    for i in range(size):
        print("*" * size)


def text_stretch():
    text = input("Enter a word: ")
    output = ""
    for i in range(len(text)):
        output += text[i] + "." * (i + 1)
    print(output)

# ladder()
# star_box()
text_stretch()