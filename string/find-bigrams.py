"""

Bigrams are pairs of consecutive words.

For example, the sentence "Have free hours and love children?" contains the following bigrams:

    (have, free), (free, hours), (hours, and), (and, love), and (love, children). 

Write a function that takes a string as input and returns a list of bigrams. 

The function should convert the input string to lowercase and remove all punctuation before generating the bigrams. 

The bigrams should be returned as a list of tuples, where each tuple contains two strings.

"""

import re


def find_bigrams(sentence):
    # Convert to lowercase and remove punctuation
    sentence = sentence.lower()
    sentence = re.sub(r"[^\w\s]", "", sentence)

    # Split sentence into words
    words = sentence.split()

    # Generate bigrams
    bigrams = [(words[i], words[i + 1]) for i in range(len(words) - 1)]

    return bigrams


print(
    find_bigrams(
        "Have free hours and love children? Drive kids to school, soccer practice and other activities."
    )
)
