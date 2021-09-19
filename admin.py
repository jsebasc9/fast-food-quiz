# Name: Juan Sebastian Calderon Cordoba
# Student Number:  10551059

# This file is provided to you as a starting point for the "admin.py" program of Assignment 2
# of Programming Principles in Semester 2, 2021.  It aims to give you just enough code to help ensure
# that your program is well structured.  Please use this file as the basis for your assignment work.
# You are not required to reference it.

# The "pass" command tells Python to do nothing.  It is simply a placeholder to ensure that the starter file runs smoothly.
# They are not needed in your completed program.  Replace them with your own code as you complete the assignment.


# Import the json module to allow us to read and write data in JSON format.
import json


# This function repeatedly prompts for input until an integer is entered.
# See Point 1 of the "Functions in admin.py" section of the assignment brief.
def input_int(prompt):
    while True:
        try:
            response = int(prompt)
            if response <= 0:
                prompt = input('Invalid input - Try again: ')
            else:
                break
        except ValueError:
            prompt = input('Invalid input - Try again: ')
            continue
        return response
    # pass



# This function repeatedly prompts for input until something other than whitespace is entered.
# See Point 2 of the "Functions in admin.py" section of the assignment brief.
def input_something(prompt):  
    while True: 
        if not prompt.strip():
            prompt = input('Invalid input - Try again: ')
        else:
            break
    # pass



# This function opens "data.txt" in write mode and writes data_list to it in JSON format.
# See Point 3 of the "Functions in admin.py" section of the assignment brief.
def save_data(data_list):
    with open('data.json', 'w') as file:
            json.dump(data_list, file, indent=4)
    pass



# Here is where you attempt to open data.txt and read the data into a "data" variable.
# If the file does not exist or does not contain JSON data, set "data" to an empty list instead.
# This is the only time that the program should need to read anything from the file.
# See Point 1 of the "Requirements of admin.py" section of the assignment brief.
data=[]
try:
    with open('data.json', 'r') as file:
        data = json.load(file)
    print(data)
except FileNotFoundError: # In case there is no file
    print('File not found, will create a new one.')
    with open('data.json', 'w') as file:  # Create a file using write/read mode
        json.dump(data, file) 

file.close()

# Print welcome message, then enter the endless loop which prompts the user for a choice.
# See Point 2 of the "Requirements of admin.py" section of the assignment brief.
# The rest is up to you.
print('Welcome to the Fast-Food Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ').lower() # Convert input to lowercase to make choice selection case-insensitive.
        
    if choice == 'a':
        # Add a new fast-food item.
        fast_food = {'name':'', 'energy':'', 'fat':'', 'protein':'', 'carbohydrates':'', 'sugars':'', 'sodium':''}
        
        # repeatedly re-prompt the user for valid input no whitespace
        fast_food['name'] = input('Enter name of fast-food item: ')
        input_something(fast_food['name']) # repeatedly re-prompt the user for valid input no whitespace         
        fast_food['energy'] = input('Enter energy in kilojoules: ')
        input_int(fast_food['energy'])
        fast_food['fat'] = input('Enter fat in grams: ')
        input_int(fast_food['fat'])
        fast_food['protein'] = input('Enter protein in grams: ')
        input_int(fast_food['protein'])
        fast_food['carbohydrates'] = input('Enter carbohydrates in grams: ')
        input_int(fast_food['carbohydrates'])
        fast_food['sugars'] = input('Enter sugars in grams: ')
        input_int(fast_food['sodium'])
        fast_food['sodium'] = input('Enter sodium in milligrams: ')

        data.append(fast_food)
        save_data(data)
        fast_food.clear()
        pass


    
    elif choice == 'l':
        # List the current fast-food items.
        # See Point 4 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 's':
        # Search the current fast-food items.
        # See Point 5 of the "Requirements of admin.py" section of the assignment brief.
        pass



    elif choice == 'v':
        # View a fast-food item.
        # See Point 6 of the "Requirements of admin.py" section of the assignment brief.
        pass

        

    elif choice == 'd':
        # Delete a fast-food item.
        # See Point 7 of the "Requirements of admin.py" section of the assignment brief.
        pass

        

    elif choice == 'q':
        # End the program.
        # See Point 8 of the "Requirements of admin.py" section of the assignment brief.
        pass



    else:
        # Print "invalid choice" message.
        # See Point 9 of the "Requirements of admin.py" section of the assignment brief.
        pass



# If you have been paid to write this program, please delete this comment.
