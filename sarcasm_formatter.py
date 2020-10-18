import re
import argh

@argh.arg('input_text',default='',nargs='?')
@argh.arg('-i', '--interactive')
def sarcasm(input_text,
	interactive=False,
	output_intro=False,
	uppercase_start=False,
	):
	"""Format an input text, sarcastically.

	Parameters
	----------

	input_text : str
		Input text to be formatted sarcastically, i.e. in alternating case.
	interactive : bool, optional
		Whether to prompt the user explicitly for input parameters.
	output_intro : bool, optional
		Whether to print the output with an intro sentence.
	uppercase_start : bool, optional
		Whether the first whitelisted character in the string should be uppercase.
	"""

	while interactive==True:
		# Request y/n from user
		uppercase_start = input('Do you want to start with upper case? [y/n]:\n> ')
		# Set starting case value according to user answer
		if uppercase_start == 'y':
			uppercase_start = True
			output_intro = True
			interactive = False
		elif uppercase_start == 'n':
			uppercase_start = False
			output_intro = True
			interactive = False

	if not input_text:
		input_text = input("Please enter the string you desire to format:\n> ")

	# Store list of all non-white-space, non-numeric characters
	list_of_chars = re.findall("[^\\s\\d\\W]", input_text)

	alternate_string = alternate(input_text, list_of_chars, uppercase_start)

	if output_intro:
		print(f'Your sarcastically formated string is:\n> {alternate_string}')
	else:
		print(alternate_string)

def alternate(input_text, list_of_chars,
	uppercase_start=False,
	):
	"""Alternate case of listed characters within an input string.

	Parameters
	----------

	input_text : str
		Input text to be formatted in alternating case.
	list_of_chars : str
		List of characters for which case changing is performed and which count towards the alternation.
	uppercase_start : bool, optional
		Whether the first whitelisted character in the string should be uppercase.
	"""

	result = ''
	next_char_upper_case = uppercase_start

	for i in range(len(input_text)):
		# Alternate each letter, skipping whitespace, numbers and punctuation
		if input_text[i] in list_of_chars:
			if next_char_upper_case == False:
				result += input_text[i].lower()
				next_char_upper_case = True
			else:
				result += input_text[i].upper()
				next_char_upper_case = False
		else:
			result += input_text[i]
	return result
