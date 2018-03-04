import random 

def rolldice():
	rand = random.randint(1, 6)
	return rand
def makeintid(num_of_rolls):
	word_id = ''
	for i in range(num_of_rolls):
		word_id += str(rolldice())
	return word_id
def pickfile(digit):
	files = ['passwordcreator/words/fourdice.txt', 'passwordcreator/words/fourdicelong.txt', 'passwordcreator/words/fivedice.txt']
	if digit == None or digit == 0:
		return files(random.randint(0,len(file)))
	return files[digit-4]
def makepassword(digitlen, num_words):
	file = pickfile(digitlen)
	password = ''
	for i in range(num_words):
		num = makeintid(digitlen)
		f = open(file, 'r')
		for line in f:
			if num == line[:digitlen]:
				word = ' '.join(line.split())[digitlen+1:]
				password += word + ' '
		f.close()
	return password.strip().replace(' ', '-')

# # MAIN Function
# if __name__ == '__main__':
# 	# Run code here
# 	numofdice = 4
# 	makepassword('words/fourdice.txt', numofdice, numofdice)
