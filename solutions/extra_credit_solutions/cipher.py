"""
Lab_Python_03
Extra Credit
Solution for Extra Credit Question 1 - Caesar Cipher
"""


unencoded_phrase = raw_input("Enter sentence to encrypt: ")
encoding_shift = int(raw_input("Enter shift value: "))

encoded_phrase = ''

for character in unencoded_phrase:

	# converting the character into an integer
	character_ascii = ord(character)
	
	if 65 <= character_ascii <= 90:
		# then it is a uppercase letter
		ascii_shift = 65
		is_letter = True
	elif 97 <= character_ascii <= 122:
		# then it is a lowercase letter
		ascii_shift = 97
		is_letter = True
	else:
		# then it is not a letter, so we pass it through unchanged 
		new_character = character
		is_letter = False

	
	if is_letter:
		
		# ascii_shift is by how much we have to shift
		# the ascii value to bring it between 0 and 25
		letter_index = character_ascii - ascii_shift

		# here we add the encoding shift, then use the 
		# modulus operator to constrain the value to 0 - 25
		new_index = (letter_index + encoding_shift) % 26
		
		# shifting the letter index back to the proper ascii range
		# and converting it back to a character
		new_character = chr(new_index + ascii_shift)

	
	# now adding the new character to the encoded phrase we are building
	encoded_phrase += new_character

print "The encoded phrase is: %s" % encoded_phrase


