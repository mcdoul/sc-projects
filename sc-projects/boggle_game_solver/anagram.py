"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""
import time
# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop
word_dict = {}
ans_words = []


def main():
    global ans_words
    print('Welcome to stanCode "Anagram Generator" (or -1 to quit)')
    while True:
        s = input('Find anagrams for: ')
        start = time.time()
        read_dictionary(s)
        if s == '-1':
            break
        print('Searching...')
        find_anagrams(s)
        print(f'{len(ans_words)} anagrams: {ans_words}')
        ans_words = {}
        end = time.time()
        print(f'time: {end-start}')


def read_dictionary(s):
    global word_dict
    with open(FILE, 'r') as f:
        for line in f:
            word = line.strip()
            if len(word) == len(s):
                word_dict[word] = 1


def find_anagrams(s):
    """
    :param s: input word
    :return: anagrams of target word
    """
    helper(s, "", len(s), {})


def helper(s, current_word, ans_len, index):
    if len(current_word) == ans_len:            # Base Case
        if current_word in word_dict and current_word not in ans_words:
            ans_words.append(current_word)
            print(f'Found:{current_word}')
            print('Searching...')
    else:
        for i in range(len(s)):
            if i not in index:
                index[i] = 1
                # choose
                current_word += s[i]
                # explore
                helper(s, current_word, ans_len, index)
                # un- choose
                current_word = current_word[:len(current_word)-1]
                index.pop(i)


if __name__ == '__main__':
    main()
