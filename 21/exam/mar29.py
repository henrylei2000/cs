def pattern(string):
    # generates patterned code based on word input
    length = len(string)
    code = []
    for a in range(length):
        letter_code = [0] * length  # reset code
        for i in range(length):
            if string[i] == string[a]:
                letter_code[i] = 1
        code += [letter_code]
    return code


def main():

    message = True
    words = ["a", "b", "c"]  # compare 1st with 2nd, 1st with 3rd

    for i in range(len(words) - 1):
        if pattern(words[i]) != pattern(words[i + 1]):
            message = False
            break
    print(message)


main()