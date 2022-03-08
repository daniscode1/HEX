'''
HEX SOURCE CODE
'''

# Importing the necessary modules
# This is used to get the user arguments
import sys
# This is used to generate random data
import random

def error(message):
    print(f'[ERROR] {message}')

################################################## Commands ##################################################
def country():
    # Read the country list
    file = open('hex/data/countries', 'r')
    countries = file.read()
    file.close()

    # Get a list of countries
    countries = countries.split('\n')

    # Randomly generate a country
    country = random.choice(countries)

    # Return the variable
    return country
def name():
    # Read the names list
    file = open('hex/data/names', 'r')
    names = file.read()
    file.close()

    # Get a list of names
    names = names.split('\n')

    # Randomly generate a country
    name = random.choice(names)

    # Return the variable
    return name
def gender():
    # Read the genders list
    file = open('hex/data/genders', 'r')
    genders = file.read()
    file.close()

    # Get a list of names
    genders = genders.split('\n')

    # Randomly generate a country
    gender = random.choice(genders)

    # Return the variable
    return gender

#################### PROFILES ####################
def profile():
    # Get all the random data and save it in to variables#
    ran_gender = gender()
    ran_name = name()
    ran_country = country()

    # Return the profile
    return f'''
    ########### 
    #(. ❛ ᴗ ❛.)#
    ###########

    \033[2;31;43m Name \033[0;0m
    {ran_name}
    \033[2;31;43m Gender \033[0;0m
    {ran_gender}
    \033[2;31;43m From \033[0;0m
    {ran_country}
    '''
#################### END ####################
################################################# END ##################################################

# Get the user arguments
usr_argv = sys.argv

# Check if the user provided more than 1 argument
if len(usr_argv) >= 2:
    # Get the user command
    usr_command = sys.argv[1]

    # Check to see what type of command it is + execute it if the command is valid else return error
    if usr_command == '-help':
        # Print out help info
        print('''
        HEX HELP
        python3 hex.py [commands: -help, -version, -random-num, -random-country, -random-name, -random-gender, -profile]
        ''')
    elif usr_command == '-version':
        # Read the file
        file = open('hex/version', 'r')
        data_version = file.read()
        file.close()

        # Print the data
        print(f'HEX {data_version}')
    elif usr_command == '-random-num':
            # Generate a random number from 1 and 1M + print it
            num = random.randint(1, 1000000)
            print(num)
    elif usr_command == '-random-country':
        print(country())
    elif usr_command == '-random-name':
        print(name())
    elif usr_command == '-random-gender':
        print(gender())
    elif usr_command == '-profile':
        print(profile())
    else:
        error('Your commend is not valid, type -help for help')
else:
    error('Please provide a command')