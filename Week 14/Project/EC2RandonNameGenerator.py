#!/usr/bin/env python3.7

# EC2 Random Name Generator
# Authored by Jason Ceballos
# 05/18/2022
# Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
# Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:

import numbers
import random
import string

# Generate random characters and numbers that will be included in the unique name.

def getEC2NameString(length):
    """Generate a random string"""
    str = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(str) for i in range(length))

print("Welcome to the EC2 Random Name Generator!")

# 1. Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.

ec2_amount = int(input("Please enter how many EC2 instance names you need: "))

# 2. Allow the user to input the name of their department that is used in the unique name.

departments = ["Marketing", "Accounting", "FinOps"]
dept_name = str(input("Please enter your department name: "))
print("Your Department is:" , dept_name)
# We only want users from the departments list we provided to use this program. Everyone else gets the print command and program exits

while ec2_amount >= 1:
    for num in range(ec2_amount):
        if dept_name != list(departments):
            print("Random EC2 Name is = ", dept_name + getEC2NameString(18))
        continue
else: 
    print("You do not have permission to run this program. Have a nice day!")
    exit()
