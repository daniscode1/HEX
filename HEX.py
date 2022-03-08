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
def phone_number():
    # +1 50 657 8193
    # Read the file with all the country codes
    file = open('hex/data/country_codes', 'r')
    country_code = file.read()
    file.close()

    # Generate a random country code
    # Create a list of country codes
    country_codes = country_code.split('\n')

    # Generate a random country code
    random_country_code = random.choice(country_codes)

    # Generate the first two numbers
    gen0 = random.randint(10, 99)

    # Generate the second three numbers
    gen1 = random.randint(100, 999)

    # Generate the last four numbers
    gen2 = random.randint(1000, 9999)

    # Combine all the numbers together & return them
    return f'{str(random_country_code)} {int(gen0)} {int(gen1)} {int(gen2)}'
def birth():
    # Random Generate Date
    date = random.randint(1, 28)

    # Random Generate Month
    month = random.randint(1, 12)

    # Random Generate Year
    year = random.randint(1980, 2010)

    # Combine them together & return them
    return f'{date}/{month}/{year}'
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
        python3 hex.py [commands: -help, -version, -random-num, 
        -random-country, -random-name, -random-gender, -random-phone-number,
        -random-birthday]
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
    elif usr_command == '-random-phone-number':
        print(phone_number())
    elif usr_command == '-random-birthday':
        print(birth())
    else:
        error('Your commend is not valid, type -help for help')
else:
    error('Please provide a command')