import re

# Ask user for desired case. Loop till he give a valid answer
while True:
    # Request y/n from user
    user_desired_case = input(
        'Do you want to start with lower case? [y/n]:\n> ')
    # Set bool value according to user answer
    if user_desired_case.lower() == 'y':
        user_start_lower = True
        break
    elif user_desired_case.lower() == 'n':
        user_start_lower = False
        break

# Request user input string
user_input = input("Please enter the string you desire to format:\n> ")

# Store list of all non-white-space, non-numeric characters
list_of_chars = re.findall("[^\\s\\d\\W]", user_input)

# Function to alternate characters througn string
def alternate(str, user_bool):
    result = ''
    next_char_upper_case = user_bool

    # Loop through string
    for i in range(len(str)):
        # Alternate each letter, skipping whitespace, numbers and punctuation
        if user_input[i] in list_of_chars:
            if next_char_upper_case == False:
                result += user_input[i].upper()
                next_char_upper_case = True
            else:
                result += user_input[i].lower()
                next_char_upper_case = False
        else:
            result += user_input[i]
    return result

# Store formatted string
alternate_string = alternate(user_input, user_start_lower)

# Print formatted string
print(f'Your sarcastically formated string is:\n> {alternate_string}')