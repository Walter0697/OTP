import random 

def xor(num1, num2):
	if num1 == num2:
		return "0"
	else:
		return "1"

def xorAll(string1, string2):
	finalstring = ""
	for i in range(len(string1)):
		finalstring += xor(string1[i], string2[i])
	return finalstring

def randomOneNum():
	return random.randint(0, 1)

def randomPad(length):
	returnObj = ""
	for i in range(length):
		returnObj += str(randomOneNum())
	return returnObj

plaintext  = "001100"		#JUST CHANGE THIS
onetimepad = randomPad(len(plaintext))
cipher 	   = xorAll(plaintext, onetimepad)
print("plain  : " + plaintext)
print("secret : " + onetimepad)
print("cipher : " + cipher)
decode 	   = xorAll(cipher, onetimepad)
print("decoded: " + decode)