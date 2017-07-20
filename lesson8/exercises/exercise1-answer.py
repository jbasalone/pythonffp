'''
Employees were given specific codes.

You need to find the code that matches the employee, using a file with specific codes called empcodes.txt

Open the file, read it, figure out who the employee is that I list here, and then write to the file the employees name that matches the code.
'''
# gets the sys module and imports the function argv
from sys import argv
# setting the arguments to be script name and the filename to be used
# so filename becomes whatever the specified filename arugement is
script, filename = argv

# a dictionary of employee codes to names with a key value pair
employee_codes = {90234876:'Jenn',
                    90237846:'Bryan',
                    90232195:'Leon',
                    90236519:'Jason',
                    90234912:'Dominic',
                    90234812:'Ben'}

# Start code below

# opening file in read only mode as variable called 'codes'
# assigning rawcodes as the rawdata thats human readable from read()
with open(filename, 'r') as codes:
    rawcodes = codes.read()

# splitting the data up on '\n' or newline character
splitcodes = rawcodes.splitlines()
# we are splitting the string in the 3rd position on a space.
tmpcodes = splitcodes[3].split(' ')
# remove the object (bad data) in the 3rd location
splitcodes.pop(3)

# looping over tmpcodes append the code to the variable splitcodes
for code in tmpcodes:
    splitcodes.append(code)

# open a new file called "codenames.txt" its been truncated and save it as the variable txtfile

with open('codenames.txt', 'w') as txtfile:
# we are gonna loop through splitcodes and make each object an integar
# we define a new variable called "name" assigning the value for the key we provide (employee_codes[code]= the key) and adding new line character
# write the value of the variable 'name' to the file
    for code in splitcodes:
        code = int(code)
        name = employee_codes[code] + '\n'
        txtfile.write(name)
