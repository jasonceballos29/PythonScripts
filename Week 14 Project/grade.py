#Grade Calculation Python Script
#Authored by Jason Ceballos
#05/18/2022

#We need to ask for user input to get the grade. Requesting it as a number (integer) so we can calculate the grade

scores = int(input("Please enter your grade in numeric format to receive a letter grade: "))

# Defining a function that will caculate the letter grade based on the number that is entered by the user 

def determine_grade(scores):
    if scores >= 90 and scores <= 100:
        return 'A'
    elif scores >= 80 and scores <= 89:
        return 'B'
    elif scores >= 70 and scores <= 79:
        return 'C'
    elif scores >= 60 and scores <= 69:
        return 'D'
    elif scores >= 50 and scores <= 59:
        return 'E'
    else:
        return 'F'

#Lastly, we will print the grade for the user

print("Your grade is a:" , determine_grade(scores))
