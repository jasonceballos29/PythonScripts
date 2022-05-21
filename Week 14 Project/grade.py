# Defining a function that will caculate the letter grade based on the number that is entered by the user 

def determine_grade(scores):
    if scores >= 90 and <= 100:
        return 'A'
    elif scores >= 80 and <= 89:
        return 'B'
    elif scores >= 70 and <= 79:
        return 'C'
    elif scores >= 60 and <= 69:
        return 'D'
    elif scores >= 50 and <= 59:
        return 'E'
    else:
        return 'F'
#Now we will ask for user input to get the grade. Requesting it as a number (integer) so we can calculate the grade

grade = int(input("Please enter your grade in numeric format to receive a letter grade: "))

#Lastly, we will print the grade for the user

print("Your grade is a", determine_grade)

