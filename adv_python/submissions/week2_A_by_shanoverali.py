"""
Submitted by: Shanoverali Saiyed 
Student ID: C0/882380
Submitted to: Vahid Hadavi
Date of submission: 13 May 2023
"""

# Problem A: Write a Python program to check if a number is a perfect square

def isPerfect(num):
    isPerfect = False
    cursor = 0

    while(num >= cursor*cursor): 
        if cursor * cursor == num:
            isPerfect = True
            break
        else:
            cursor = cursor + 1

    return isPerfect

a = int(input('Enter a number:'))
print("The number is :", isPerfect(a))

