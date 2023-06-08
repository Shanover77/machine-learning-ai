"""
Submitted by: Shanoverali Saiyed 
Student ID: C0/882380
Submitted to: Vahid Hadavi
Date of submission: 13 May 2023
"""

# Problem B: Write a Python program to find a missing number from a list. 

# Note : 
# Aassuming the numbers are ordered, there is only 1 number missing, and list does not always start from 1
# two conditions are always twue here, first and last number can neveer be missing since it is an ordered list and only 1 number is missing

def find_missing(list, size):
    cursor = 1
    missing = 'not found'

    while cursor < size:
        if list[cursor] != list[cursor-1]+1:
            missing = list[cursor-1]+1
        
        cursor = cursor + 1

    return missing

# begin
nums = []
num_size = int(input("How many numbers will you add in this array ? "))
print('Cool, just omit a number. I will find it !')

cursor = 0
while cursor < num_size:
   l=int(input('Enter number:'))
   nums.append(l)
   cursor = cursor + 1

print('You entered:',nums)

missing = find_missing(nums,num_size)
print('Missing number is:',missing)