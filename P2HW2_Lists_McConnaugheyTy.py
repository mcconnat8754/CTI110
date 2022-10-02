# CTI-110
# P2HW2 - List
# Ty McConnaughey
# 1/10/22
#

#add inputs labeled "Enter grade for Module __" for modules 1-6
#create a list of the variables
#drop line
#display "------------Results------------"
#display the Lowest and Highest grades
#display the sum of the grades
#display average
#display "----------------------------------------"
#align the results

module1 = float(input("Enter grade for Module 1:"))
module2 = float(input("Enter grade for Module 2:"))
module3 = float(input("Enter grade for Module 3:"))
module4 = float(input("Enter grade for Module 4:"))
module5 = float(input("Enter grade for Module 5:"))
module6 = float(input("Enter grade for Module 6:"))

module_grades = [module1, module2, module3, module4, module5, module6]

print('')
print('------------Results------------')
print(f'Lowest Grade:       {min(module_grades)}')
print(f'Highest Grade:      {max(module_grades)}')
print(f'Sum of Grades:      {sum(module_grades)}')
print(f'Average:            {sum(module_grades) / len(module_grades)}')
print('----------------------------------------')
