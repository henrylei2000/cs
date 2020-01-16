"""
 This is the loop program over string
 Henry Lei
 Spring 2020
"""


def syllable():
    word = input("Enter your word: ").lower()
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    syllable_count = 0
    # rule: the first vowel counts
    if word[0] in vowels:
        syllable_count = 1
    for i in range(1, len(word)):
        # rule: no continuous vowels
        if (word[i] in vowels) and (word[i - 1] not in vowels):
            syllable_count += 1
    # rule: ending e is not a syllable
    if word.endswith("e"):
        syllable_count -= 1
    # rule: a word has at least one syllable
    if not syllable_count:
        syllable_count = 1
    print("%s has %d syllable(s)." % (word, syllable_count))


syllable()
