#Number Guessing Game
#Authored by Jason Ceballos
#05/18/2022

#We will set the variable to our desired number. The user doesn't see or know this. This is for our reference.

right_number = 7

#This will ask the user for input for their guess.
#Users will then be able to input an integer continuously until the guess the hidden number correctly. 
#The program should respond with whether the integer entered is higher, lower, or equal to the random integer.


user_input = int(input('Welcome to the Number Guessing Game! Please enter a number: '))

run = True
while run:       
        if user_input == 7:
            print('You won! Thanks for playing!!')
            run = False 
            break
        if user_input < 7:
            print('Guess too low! Please try again.')
            user_input = int(input('Please enter a number: '))
        if user_input > 7:
            print('Guess too high! Please try again.')
            user_input = int(input('Please enter a number: '))
