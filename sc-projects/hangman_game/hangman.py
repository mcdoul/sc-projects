"""
File: hangman.py
Name: Charlotte Yang
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    This program plays hangman game. Users try to correctly figure the un-dashed word out
    by inputting one character each round.
    Players have N_TURNS chances to try and win this game.
    """
    word = random_word()
    input_ch='_'
    ans=''
    life=0
    for i in range(len(word)):
        ans=ans+'_'
    while life!=N_TURNS:
        if ans != word:
            print('The word looks like:'+ans)
            print('You have '+str(N_TURNS-life)+ ' guesses left.')
            while True:
                input_ch =input('Your guess: ')
                if not input_ch.isalpha()or len(input_ch)>1:
                    print('Illegal format!')
                else:
                    break
            input_ch=input_ch.upper()
            input_chs = ''
            last_ans = ans
            for i in range(len(word)):
                input_chs += input_ch  # make a string with input_ch in the same length with word
            ans = ''
            for i in range(len(word)):
                if input_chs[i] == word[i]:
                    if last_ans[i] == '_' or input_chs[i]:
                        ans += word[i]
                else:
                    if last_ans[i] == '_':
                        ans += '_'
                    else:
                        ans += last_ans[i]
            if ans == last_ans:
                if word.find(input_ch)!=-1:  # input same correct letter
                    print('You are correct!')
                else:  # input wrong letter
                    print('There is no ' + str(input_ch) + '\'s in the word!')
                    life+=1
            else:
                print('You are correct!')
            hangman(life)
        else:
            break # guess the right word within 7 times
    if ans == word:
        print('You win!')
        print('The word was: ' + str(word))
    else:
        print('You are completely wrong:(')
        print('The word was: ' + str(word))


def hangman(life):
    """
    draw the hangman when entering wrong letters
    """
    if life==0:
        print('-----\n'
              '|  |\n'
              '|\n'
              '|\n'
              '|\n'
              '|\n'
              '-')
    elif life==1:
        print('-----\n'
             '|  |\n'
             '|  O\n'
             '|\n'
             '|\n'
             '|\n'
             '-')
    elif life==2:
        print('-----\n'
              '|  |\n'
              '|  O\n'
              '|  |\n'
              '|\n'
              '|\n'
              '-')
    elif life==3:
        print('-----\n'
              '|  |\n'
              '|  O\n'
              '|  |\n'
              '|  |\n'
              '|\n'
              '-')
    elif life==4:
        print('-----\n'
              '|  |\n'
              '|  O\n'
              '| \\|\n'
              '|  |\n'
              '|\n'
              '-')
    elif life==5:
        print('-----\n'
              '|  |\n'
              '|  O\n'
              '| \\|/\n'
              '|  |\n'
              '|\n'
              '-')
    elif life==6:
        print('-----\n'
              '|  |\n'
              '|  O\n'
              '| \\|/\n'
              '|  |\n'
              '| /\n'
              '-')
    else:
        print('-----\n'
              '|  |\n'
              '|  O\n'
              '| \\|/\n'
              '|  |\n'
              '| / \\\n'
              '-')


def random_word():
    """
    :return: str, the word that has been randomly chosen
    """
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
