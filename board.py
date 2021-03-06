''' First of all, I learned a ton from this website: https://docs.python.org/3/library/functions.html
I wouldn't have done this without it.
References for how I learned about itertools:
https://docs.python.org/3/library/itertools.html
https://www.geeksforgeeks.org/python-itertools/ '''
import random
''' I used the random module to address an issue I saw that was not mentioned in the lab. You can find its usage I gave it in lines 105 and 113. The problem is that 
the user might enter a non numeric value such as a letter or a symbol and it would cause an error, but the lab does not mention we have to fix this so I did it 
anyways. So my solution was to generate a random number for the player in the case they did not enter a number in the given range '''
import itertools

# This function checks to see if anyone has won the match
def final(active_match):
	# This nested function helps me take less space and it analyzes each value to determine if there is a winner
	def search(l):
		if l.count(l[0]) == len(l) and l[0] != 0:
			return True
		else:
			return False

	# This is the row win finder
	for row in active_match:
		if search(row):
			print(f"Player {row[0]} wins. Game Over!")
			return True

	# This is the diagonal in the direction "/" finder
	diagonal = []
	for column, row in enumerate(reversed(range(len(active_match)))):
		diagonal.append(active_match[row][column])
	if search(diagonal):
		print(f"Player {diagonal[0]} wins. Game Over!")
		return True

	# This is the diagonal in the direction "\" finder
	diagonal = []
	for ix in range(len(active_match)):
		diagonal.append(active_match[ix][ix])
	if search(diagonal):
		print(f"Player {diagonal[0]} wins. Game Over!")
		return True

	# This is the column win finder
	for column in range(len(active_match)):
		vertical = []
		for row in active_match:
			vertical.append(row[column])
		if search(vertical):
			print(f"Player {vertical[0]} wins. Game Over!")
			return True

	# This is the tie finder
	for row in active_match:
		for column in row:
			if column == 0:
				return False
	print("Draw. Game Over!")

	return False



''' This function prints the board, at first I tried imitating the one in the project lab video like this: x = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
but I kept getting string-related errors so I opted for this instead: x = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]'''
# For this same reason I used "1" and "2" as markers instead of "x" and "o"
def game_board(print_board, player=0, row=0, column=0, active=False):

	# My "try and except" reference: https://pythonbasics.org/try-except/. I learned this because I read that it helps with error handling
	try:
		if print_board[row][column] != 0:
			print(f"**** Board {[select_column], [select_row]} has already been selected. Please place somewhere else on the board ****")
			print("**** Invalid choice. Please mark again! ****")
			return print_board, False
		if not active:
			print_board[row][column] = player
		for row in print_board:
			print(row)
		return print_board, True
	except IndexError: # Here is what I used "try and except" it for
		print(f"**** Invalid row or column. Please select row/column between values 0 to 2 ****")
		print("**** Invalid choice. Please mark again! ****")
		return print_board, False

# This section basically keeps the program running using while loops, I separted the while loops to make it easier to read
start = True
while start:
	board_grid = 3
	total_players = 2
	match = [[0 for i in range(board_grid)] for i in range(board_grid)]
	players = list(range(1,total_players+1))
	end_game = False
	match, _ = game_board(match, active=True)
	player_cycle = itertools.cycle(players)

	while not end_game: # This section cycles through players
		player_turn = next(player_cycle)
		print(f"Player {player_turn}, make your move.")
		next_turn = False

		while not next_turn:
			try: # This section handles column input and display
				select_column = int(input(f"Enter column number (0-2): "))
			except ValueError:
				print(f"Only numbers in range (0-2) are allowed. A random column number will be selected")
				select_column = random.randrange(board_grid) # <-- This is what I was referring to at the start of the file.
				print(f"Column number selected: {select_column}")
				print()

			try: # This section handles row input and display
				select_row = int(input(f"Enter row number (0-2): "))
			except ValueError:
				print(f"Only numbers in range (0-2) are allowed. A random row number will be selected")
				select_row = random.randrange(board_grid) # <-- This is what I was referring to at the start of the file.
				print(f"Row number selected: {select_row}")
				print()
			# This section just displays what column and row the player selected
			print(f"Player {player_turn} added mark at the location {select_column, select_row}")
			print()
			match, next_turn = game_board(match, player_turn, select_row, select_column)  # This line loops player input on the board

		if final(match):  # This block ends the game if there is a winner
			end_game = True
			start = False