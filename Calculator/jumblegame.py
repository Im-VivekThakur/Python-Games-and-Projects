#import 
import random
def choose():
#words list
	words = ['rainbow', 'computer', 'science', 'programming',
			'mathematics', 'player', 'condition', 'reverse',
			'water', 'board', 'geeks']

	# random choice
	pick = random.choice(words)

	return pick


# function jumble is defined
def jumble(word):
	# sample() method to jumble characters of the word
	random_word = random.sample(word, len(word))

	# join() method to join the elements

	jumbled = ''.join(random_word)
	return jumbled


# show final score
def thank(p1n, p2n, p1, p2):
	print(p1n, 'Your score is :', p1)
	print(p2n, 'Your score is :', p2)

	# check whether won
	check_win(p1n, p2n, p1, p2)

	print('Thanks for playing...')


# Function for declaring winner
def check_win(player1, player2, p1score, p2score):
	if p1score > p2score:
		print("winner is :", player1)
	elif p2score > p1score:
		print("winner is :", player2)
	else:
		print("Draw..Well Played guys..")


# Function for playing the game.
def play():
	# enter player1 and player2 name
	p1name = input("player 1, Please enter your name :")
	p2name = input("Player 2 , Please enter your name: ")

	# variable for counting score.
	pp1 = 0
	pp2 = 0

	# variable for counting turn
	turn = 0

	# keep looping
	while True:

		# choose() function calling
		picked_word = choose()

		# jumble() function calling
		qn = jumble(picked_word)
		print("jumbled word is :", qn)

		# checking turn is odd or even
		if turn % 2 == 0:

			# if turn no. is even
			# player1 turn
			print(p1name, 'Your Turn.')

			ans = input("what is in your mind? ")

			# checking ans is equal to picked_word or not
			if ans == picked_word:

				# incremented by 1
				pp1 += 1

				print('Your score is :', pp1)
				turn += 1

			else:
				print("Better luck next time ..")

				# player 2 turn
				print(p2name, 'Your turn.')

				ans = input('what is in your mind? ')

				if ans == picked_word:
					pp2 += 1
					print("Your Score is :", pp2)

				else:
					print("Better luck next time...correct word is :", picked_word)

				c = int(input("press 1 to continue and 0 to quit :"))

				# checking the c is equal to 0 or not
				# if c is equal to 0 then break out
				# of the while loop o/w keep looping.
				if c == 0:
					# thank() function calling
					thank(p1name, p2name, pp1, pp2)
					break

		else:

			# if turn no. is odd
			# player2 turn
			print(p2name, 'Your turn.')
			ans = input('what is in your mind? ')

			if ans == picked_word:
				pp2 += 1
				print("Your Score is :", pp2)
				turn += 1

			else:
				print("Better luck next time.. :")
				print(p1name, 'Your turn.')
				ans = input('what is in your mind? ')

				if ans == picked_word:
					pp1 += 1
					print("Your Score is :", pp1)

				else:
					print("Better luck next time...correct word is :", picked_word)

					c = int(input("press 1 to continue and 0 to quit :"))

					if c == 0:
						# thank() function calling
						thank(p1name, p2name, pp1, pp2)
						break

			c = int(input("press 1 to continue and 0 to quit :"))
			if c == 0:
				# thank() function calling
				thank(p1name, p2name, pp1, pp2)
				break


# Driver code
if __name__ == '__main__':
	
	# play() function calling
	play()
