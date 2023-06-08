"""
Submitted by: Shanoverali Saiyed 
Student ID: C0/882380
Submitted to: Vahid Hadavi
Date of submission: 13 May 2023
"""

# Problem C: Write a Python program to find the single number in a list that doesn't occur twice. 

def findSingleOccurence(list, size):
    cursor = 0
    singleOccurence = None

    while cursor < size:
        currentNum = list[cursor]
        numHits = 0

        innerCursor = 0
        while innerCursor < size:
            innerNum = list[innerCursor]

            if currentNum == innerNum:
                numHits = numHits + 1

            innerCursor = innerCursor + 1
        cursor = cursor + 1

        if numHits == 1:
            singleOccurence = currentNum
        
    return singleOccurence

# begin
nums = []
num_size = int(input("How many numbers will you add in this array ? "))
print('Cool, just keep a number once, rest can occur twice. I will find it!')

cursor = 0
while cursor < num_size:
   l=int(input('Enter number:'))
   nums.append(l)
   cursor = cursor + 1

print('You entered:',nums)

single = findSingleOccurence(nums,num_size)
print('Single occurence number is:',single)