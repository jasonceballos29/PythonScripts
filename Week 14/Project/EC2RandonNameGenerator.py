#!/usr/bin/env python3.7

#EC2 Random Name Generator
#Authored by Jason Ceballos
#05/18/2022
# Several departments share an AWS environment. You need to ensure that the EC2s are properly named and are unique so team members can easily tell who the EC2 instances belong to. 
# Use Python to create your unique EC2 names that the users can then attach to the instances. The Python Script should:

import random
import string

departments = ["Marketing", "Accounting", "FinOps"]

# 1. Allow the user to input how many EC2 instances they want names for and output the same amount of unique names.

ec2_amount = int(input("Please enter how many EC2 instance names you need: "))

# 2. Allow the user to input the name of their department that is used in the unique name.

dept_name = str(input("Please enter your department name: "))

# 3. Generate random characters and numbers that will be included in the unique name.

randomstring = ''.join(dept_name + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(24))
print(randomstring)