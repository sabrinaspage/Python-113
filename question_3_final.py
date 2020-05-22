#Sabrina Reyes
'''
Suppose you are given a text file. Design a Python3 program to encrypt/decrypt that text file as follows:
If the character is an upper case character then shift that character forward, s characters forward in the alphabet.
If the character is an lower case character then shift that character backwards, s characters backwards in the alphabet.
If the character is a numeric character then shift that character also backwards, s characters backwards in the 1-digit numbers set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.
You must design two functions; one to encrypt. The other one is to decrypt. All white
space and punctuation marks must be ignored(cannot be changed). If you reach Z, or
A, the shifting may continue as a cycle(A comes after Z, Z comes before A). Both files
(original text file and the encrypted text file) must be stored in the working directory of
Python.
An example;
Let s=1 and the text file:
11300Hello World
Then encoded text file;
00299Idkkn Xnqkc
'''
import string

#let's create a file & read a file

lowerAlpha = string.ascii_lowercase
upperAlpha = string.ascii_uppercase
numbers = {0,1,2,3,4,5,6,7,8,9}

#encrypt - take the text and cipher it
def encrypt(file):
	filedata = ""
	with open(file, "r") as g:
		for line in g:
			for char in line:
				if char == 'Z':
						filedata += 'A'
				elif char.isupper() and (char != 'Z'):
					#get index of character in string
					old_char = upperAlpha.index(char)
					#now get the index -1
					old_char += 1
					#now make sure you get the character represented in that index
					new_char = upperAlpha[old_char]
					#replace the character in the line
					filedata += new_char
				elif char == 'a':
					filedata += 'z'
				elif char.islower() and (char != 'a'):
					old_char = lowerAlpha.index(char)
					old_char -= 1
					new_char = lowerAlpha[old_char]
					filedata += new_char
				#if 0, then remain at 0 bc otherwise it's negative
				elif char.isdigit():
					numerical_char = int(char)
					numerical_char -= 1
					new_char = str(numerical_char)
					filedata += new_char
				#i did not add all logograms available lol
				elif char == " " or char == "." or char == "," or char=='\n':
					filedata += char
	with open(file, 'w') as file:
		file.write(filedata)

#THIS IS THE ENCRYPTED FILE USED
encrypt("demofile_enc.txt")

#decrypt - take the ciphered text and put it back to original
#basically the opposite of the above program
def decrypt(file):
	filedata = ""
	with open(file, "r") as g:
		for line in g:
			for char in line:
				if char == 'A':
						filedata += 'Z'
				elif char.isupper() and (char != 'A'):
					#get index of character in string
					old_char = upperAlpha.index(char)
					#now get the index -1
					old_char -= 1
					#now make sure you get the character represented in that index
					new_char = upperAlpha[old_char]
					#replace the character in the line
					filedata += new_char
				elif char == 'z':
					filedata += 'a'
				elif char.islower() and (char != 'z'):
					old_char = lowerAlpha.index(char)
					old_char += 1
					new_char = lowerAlpha[old_char]
					filedata += new_char
				elif char.isdigit():
					numerical_char = int(char)
					numerical_char += 1
					new_char = str(numerical_char)
					filedata += new_char
				elif char == " " or char == "." or char == "," or char == '\n':
					filedata += char
	with open(file, 'w') as file:
		file.write(filedata)
#you can test if the below works if you want.
#decrypt("demofile_enc.txt")