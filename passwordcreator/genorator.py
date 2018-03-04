import random 

def RollDice():
	rand = random.randint(1, 6)
	return rand
def MakeIntID(num_of_rolls):
	word_id = ''
	for i in range(num_of_rolls):
		word_id += str(RollDice())
	return word_id
def MakePassword(f, digitlen, num_words):
	password = ''
	for i in range(num_words):
		num = MakeIntID(digitlen)
		f = open('words/fourdice.txt', 'r')
		for line in f:
			if num == line[:digitlen]:
				word = ' '.join(line.split())[digitlen+1:]
				password += word + ' '
		f.close()
	print password.strip().replace(' ', '-')

# MAIN Function
if __name__ == '__main__':
	# Run code here
	numofdice = 4
	MakePassword('words/fourdice.txt', numofdice, numofdice)
