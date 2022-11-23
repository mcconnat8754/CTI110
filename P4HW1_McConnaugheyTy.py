# CTI-110
# P4HW1 - Score List
# Ty McConnaughey
# 11/22/22
# make variable for question number
# make empty list for grades
# make input for amount of questions and assign it to a variable
# make loop to ask questions based on the previously made variable and add input to variable
# if entered number is below zero or over 100 print INVALID Score entered!!!! (drop line)Score should be between 0 and 100 
# drop 2 lines
# print --------------Results-----------
# print "Lowest Score  :" and the lowest grade
# remove lowest grade and print "Modified List :" and the new list
# print "Scores Average:" and the average grade
# create statements to determine what letter grade matches the average grade and attatch a variable to it
# print "Grade         :" and the variable
# print ----------------------------------


questionnum = 1
grades = []
scorenum = int(input("How many scores do you want to enter? "))

for i in range(scorenum):
    grade = int(input(f'Enter score #{questionnum} '))
    if 0 <= grade <= 100:
        grades.append(grade)
        questionnum += 1
    else:
        print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        grade = int(input(f'Enter score #{questionnum} again: '))
        grades.append(grade)
        questionnum += 1 
print('')
print('')
lowest = min(grades)
print("--------------Results-----------")
print(f'Lowest Score  : {lowest}')
grades.remove(lowest)
print(f'Modified List : {grades}')
avggrade = sum(grades) / len(grades)
print(f'Scores Average: {avggrade}')
if avggrade >= 90:
    letter = 'A'
elif avggrade >= 80:
    letter = 'B'
elif avggrade >= 70:
    letter = 'C'
elif avggrade >= 60:
    letter = 'D'
else:
    letter = 'F'
print(f'Grade         : {letter}')
print("----------------------------------")
