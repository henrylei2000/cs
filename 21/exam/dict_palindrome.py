"""
This is an OPTIONAL EXTRA CHALLENGE

Program that reads from a dictionary file, finds and prints all palindromatic
words, and finds and prints the longest one.
"""

# TDD: list of features
# - read dictionary file
# - create a list of palindromatic words
# - identify the longest palindrome and its length
# - display the longest palindrome and its length



# - read dictionary file
def read(filename):
    """
    purpose: read file and return list of words
    params:
        filename (file)
    return (list): list of words
    """
    # Passing "r" opens the file for reading
    file = open(filename, "r")
    # - create a list of words
    words = []
    for line in file:
        words.append(line.rstrip('\n'))

    file.close()

    return words


# - sanitize input word
def sanitize(string):
    edited = ''
    for letter in string:
        if letter.isalpha():
            edited += letter
    return edited


# check if string is symmetric
def is_palindrome(string):
    # check if string is symmetric
    if len(string) == 0:  # base case
        return True
    if string[0] != string[len(string) - 1]:
        return False
    else:
        # change parameter for recursive call
        return is_palindrome(string[1:len(string) - 1])


# - create a list of palindromatic words
def build_palindromes(words):
    """
    purpose: create a list of palindromes
    params:
        words (list)
    return (list): list of palindromes
    """
    palindromes = []  # accumulator pattern
    for word in words:
        # ignore upper initial, length == 1
        sanitized = sanitize(word)
        if len(sanitized) > 1 and not sanitized[0].isupper():
            if is_palindrome(sanitized):
                palindromes.append(word)

    return palindromes


# - identify the longest palindrome and its length
def find_longest(palindromes):
    """
    purpose: find longest palindrome and its length from list
    params:
        palindromes (list)
    return (list of str): longest palindromes
    """
    longest = 0
    for palindrome in palindromes:
        if len(palindrome) > longest:
            longest = len(palindrome)

    # now we have the value of longest, let's accumulate list of longest palindrome(s)
    longest_palindromes = []
    for palindrome in palindromes:
        if len(palindrome) == longest:
            longest_palindromes.append(palindrome)

    return longest_palindromes


# - display the longest palindrome and its length
def display(palindromes, longest):
    """
    purpose: display results
    params:
        palindromes (list)
        longest (list)
    return (none)
    """
    print("Found %d palindromatic words in dictionary" % len(palindromes))
    print(palindromes)
    if len(longest) == 0:
        print("There are no palindromatic words.")
    elif len(longest) == 1:
        print("The longest palindromatic word is %s with length %d" % (longest[0], len(longest[0])))
    else:  # multiple words with same longest length
        print("Below are the longest words with length %d:" % len(longest[0]))
        print(longest)


def main():

    # - read dictionary file
    file = "test"
    words = read(file)

    # - build a list of palindromatic words
    palindromes = build_palindromes(words)

    # - identify the longest palindrome and its length
    longest_palindromes = find_longest(palindromes)

    # - display the longest palindrome and its length
    display(palindromes, longest_palindromes)


main()

