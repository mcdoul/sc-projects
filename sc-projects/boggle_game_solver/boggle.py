"""
File: boggle.py
Name: Charlotte Yang
----------------------------------------
TODO:The program plays boggle game.
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
word_lst = {}  # words list from 'dictionary.txt'
count = 0      # the number of words been found


def main():
	"""
	The program plays boggle game.
	"""
	read_dictionary()
	board = {}
	switch = True
	for i in range(4):
		row = input(f'{i+1} row of letters: ').lower().split()
		if len(row) != 4:  # wrong input number
			print('Illegal Input')
			break
		else:
			for j in range(4):
				if len(row[j]) != 1:  # wrong input format
					print('Illegal Input')
					switch = False
					break
				else:
					# add input in to word-board
					board[(j, i)] = row[j]
		if switch is False:   # wrong input format
			break
	if len(board) == 16:
		boggle(board)
		print(f'There are {count} words in total.')


def boggle(board):
	"""
	:param board: (dict) A 4x4 word-board with x-coordinate and y-coordinate of each grid(letter)
	:return: no return
	"""
	for x in range(4):
		for y in range(4):
			boggle_helper(board, board[(x, y)], [], x, y, [(x, y)])


def boggle_helper(board, current_word, ans_lst, x, y, used_lst):
	"""
	:param board: (dict) A 4x4 word-board with x-coordinate and y-coordinate of each grid(letter)
	:param ans_lst: list of words been found
	:param x: x-coordinate of the letter
	:param y: y-coordinate of the letter
	:param current_word: the words being checked
	:param used_lst: the x-coordinate and y-coordinate of checked letters
	:return: no return
	"""
	global count
	if has_prefix(current_word):
		# Base case
		if len(current_word) >= 4 and current_word in word_lst:
			if current_word not in ans_lst:
				ans_lst.append(current_word)
				del word_lst[current_word]
				print('Found: ' + current_word)
				count += 1
				boggle_helper(board, current_word, ans_lst, x, y, used_lst)
		else:
			for i in range(-1, 2, 1):
				for j in range(-1, 2, 1):
					if 0 <= x+i <= 3 and 0 <= y+j <= 3 and (x+i, y+j) not in used_lst:
						# choose
						current_word += board[(x+i, y+j)]
						used_lst.append((x+i, y+j))
						# explore
						boggle_helper(board, current_word, ans_lst, x+i, y+j, used_lst)
						# un-choose
						current_word = current_word[:len(current_word) - 1]
						used_lst.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	global word_lst
	with open(FILE, 'r') as f:
		for line in f:
			word = line.strip()
			if len(word) >= 4:
				word_lst[word] = 1


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	global word_lst
	for word in word_lst.keys():
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
