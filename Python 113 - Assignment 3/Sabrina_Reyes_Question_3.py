#Sabrina Reyes
#Assignment 3
#Question 3
'''
Write a Python3 function to check if the given file object (a
parameter) contains any words that have the vowels in alphabetical
order. For example: abstemious, facetious etc. If it contains any
word that has this property, your program must print the word and
byte location (or line) of the word in the file.
'''

fn = open('alphabetical.txt', 'w')

fn.write("abstemious abstemiously celery faint wet"\
		 "anteriourly wave unbiased tiger\n"\
		 "materious tragedious rid lackadaisical travertinous\n"\
		 "avenious balance smoggy waste facetious\n"\
		 "aerious squalid rustic affectious anemious\n"\
		 "uninterested abstenious acheilous\n")

fn.close()
f = open('alphabetical.txt', 'r')

#check if all the vowels exists in the word in the first place
def check(string):
	string = string.lower()
	vowels = set("aeiou")
	s = set({})

	#loop through every character in string
	for char in string:
		#if the character in the vowels set exists
		if char in vowels:
			#add it to the set
			s.add(char)
		else:
			pass
	#compare the length of s to length of vowels
	if len(s) == len(vowels):
		return True
	else:
		return False

#check if the vowels are in order
def inorder(string):
	c = chr(64)
	for i in range(len(word)):
		if(word[i] == 'a' or word[i] == 'e' or word[i] == 'i' or word[i] == 'o' or word[i] == 'u'):
			#check if the letter is less than the stored value
			if (word[i] < c):
				return False
			#store the vowel to check for the next iteration
			else:
				c = word[i]
	return True;

#check for the line by opening the read file and finding if the word is in the line of the position
for line in f:
	for word in line.split(): #split the line apart by space
		arr = ['a','e','i','o','u']
		if(check(word)):
			if(inorder(word)):
				with open('alphabetical.txt', 'r') as myFile:
					for pos, line in enumerate(myFile, 1):
						if word in line:
							print(str(word) + " is on line " + str(pos))