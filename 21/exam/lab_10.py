"""
Program to check whether user-entered editeds are palindromes.
"""


# TDD: list of features
# get string from user
# delete unnecessary characters in string
# check if string is symmetric
# display message clarifying result

# delete unnecessary characters in string
def sanitize(string):
    edited = ''
    for letter in string.lower():
        if letter in "abcdefghijklmnopqrstuvwxyz":
            edited += letter
    return edited


# check if string is symmetric
def is_palindrome(string):
    # check if string is symmetric
    if len(string) == 0:
        return True
    if string[0] != string[len(string) - 1]:
        return False
    else:
        return is_palindrome(string[1:len(string) - 1])


def main():
    finish = False  # flag pattern
    while not finish:
        # get string from user
        string = input("Enter some text (or 'quit'): ")

        if string == "quit":
            print("Goodbye")
            finish = True
        else:
            # delete unnecessary characters in string
            edited = sanitize(string)

            # check if string is symmetric
            palindrome = is_palindrome(edited)

            # display message clarifying result
            if palindrome:
                print("This is a palindrome!")
            else:
                print("This is NOT a palindrome.")


main()

