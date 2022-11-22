# CTI-110
# P4HW1 - Score List
# Ty McConnaughey
# 11/22/22
# make variable for question number
# make empty list for grade
# make input for amount of questions and assign it to a variable
# make loop to ask questions based on the previously made variable and add input to variable
# if entered number is below zero or over 100 print 




questionnum = 1
grades = []
scorenum = int(input("How many scores do you want to enter? "))

for i in range(scorenum):
    grade = int(input(f'Enter score #{questionnum} '))
    if 0 <= score <= 100:
        grades.append(grade)
        x += 1
    else:
        print("\nINVALID Score entered!!!!\nScore should be between 0 and 100")
        grade = int(input(f'Enter score #{questionnum} again: '))
        grades.append(grade)
        x += 1 

print(grades)

