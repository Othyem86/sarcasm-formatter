import re

# Declare basic variables
loop_until_dum_dum_gets_it = True
user_start_lower = False

# Ask user for desired case. Loop till he give a valid answer
while loop_until_dum_dum_gets_it:
    # Request y/n from user
    user_desired_case = input('Do you want to start with lower case? [y/n]:\n')
    # Set bool value according to user answer
    if user_desired_case.lower() == 'y':
        user_start_lower = True
        break
    elif user_desired_case.lower() == 'n':
        user_start_lower = False 
        break

# Request user input string
user_input = input("Please enter the string you desire to format:\n")

# Store list of all non-white-space, non-numeric characters
just_character_list = re.findall("[^\s^\d]", user_input)
# Function to alternate characters througn string
def alternate(str, user_bool):
    # Declare basic function variables
    result = ''
    start_lower_case = user_bool

    # Loop through string and alternate
    for i in range(len(str)):
        if user_input[i] in just_character_list:
            if start_lower_case == False:
                result += user_input[i].upper()
                start_lower_case = True
            else:
                result += user_input[i].lower()
                start_lower_case = False
        else:
            result += user_input[i]
    return result

# Store formatted string
alternate_string = alternate(user_input, user_start_lower)

# Print formatted string
print(f'Your sarcastically formated string is: \n{alternate_string}')
