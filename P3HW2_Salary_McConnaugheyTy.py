# CTI-110
# P3HW2 - Salary
# Ty McConnaughey
# 1/11/22
#
# make variables and input for name, work hours, and pay rate
# display name
# calculate if employee worked overtime
# calculate overime pay if they did
# calculate normal pay
# add them

name = input("Enter employees's name:" )
work_hours = float(input("Enter number of hours worked:" ))
pay_rate = float(input("Enter employees's pay rate:" ))
#math stuff
if work_hours > 40.0:
    overtime = work_hours - 40.0
overtime_pay = (pay_rate * 1.5) * overtime
print("-----------------------------------")
print(f'Employee name:   {name}')
print("")



