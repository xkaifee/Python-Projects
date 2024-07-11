"""
Author: Xaen, xkaifee@purdue.edu
Assignment: 09.4 - File Analysis
Date: 10/29/2023

Description:
    This program reads two files and analyzes them. 
    It finds the frequency of the words in the files, the common words in both files, 
    and the words that are in either file but not both.

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
import string

"""Write new functions below this line (starting with unit 4)."""
def get_words(filename): # This function gets the words from the file and returns them in a list
    with open(filename, 'r') as f:
        text = f.read().lower() # This line reads the file and makes all the letters lowercase
        words = text.split()
        words = [w.strip(string.punctuation) for w in words]
        return words

def get_word_frequency(words): # This function gets the frequency of the words and returns them in a dictionary
    word_frequency = {}
    for word in words: # This loop checks if the word is in the dictionary and if it is not, it adds it to the dictionary and sets the value to 1. If it is in the dictionary, it adds 1 to the value
        if word not in word_frequency:
            word_frequency[word] = 1
        else:
            word_frequency[word] += 1
    return word_frequency


def main():

    python_1_words = get_words('python_1.txt') # This line gets the words from the file and returns them in a list
    python_1_word_frequency = get_word_frequency(python_1_words) # This line gets the frequency of the words and returns them in a dictionary


    python_2_words = get_words('python_2.txt') # This line gets the words from the file and returns them in a list
    python_2_word_frequency = get_word_frequency(python_2_words)    # This line gets the frequency of the words and returns them in a dictionary


    common_words = set(python_1_word_frequency.keys()) & set(python_2_word_frequency.keys())


    eitherbutnotboth_words = set(python_1_word_frequency.keys()) ^ set(python_2_word_frequency.keys())


    with open('python_1_word_frequency.txt', 'w') as f: # This line writes the words and their frequency to a file
        for word in sorted(python_1_word_frequency.keys()): # This loop sorts the words in alphabetical order
            f.write(f"{word}: {python_1_word_frequency[word]}\n")

    with open('python_2_word_frequency.txt', 'w') as f:
        for word in sorted(python_2_word_frequency.keys()):
            f.write(f"{word}: {python_2_word_frequency[word]}\n")

    with open('common_words.txt', 'w') as f:
        for word in sorted(common_words):
          f.write(f"{word}\n")

    with open('eitherbutnotboth.txt', 'w') as f:
        for word in sorted(eitherbutnotboth_words):
         f.write(f"{word}\n")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
