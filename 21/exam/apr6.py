def is_vowel(letter):

    letter = letter.lower()

    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        return True
    else:
        return False


def main():
    result = is_vowel("ed")
    print(result)


main()


