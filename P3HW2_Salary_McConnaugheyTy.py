# CTI-110
# P3HW2 - Salary
# Ty McConnaughey
# 1/11/22
#
# make variables and input for name, work hours, and pay rate
# calculate if employee worked overtime
# calculate overime pay if they did
# calculate normal pay
# add them
# display -----------------------------------
# display Employee name: (name)
# on the same line display Hours Worked Payrate OverTime OverTime Pay RegHour Pay and Gross Pay
# put a line of ----- under that
# display and aline the corrosponding variable

name = input("Enter employees's name:" )
work_hours = float(input("Enter number of hours worked:" ))
pay_rate = float(input("Enter employees's pay rate:" ))
#math stuff
if work_hours > 40.0:
    overtime = work_hours - 40.0
else: overtime = 0.0

if overtime > 0.0:
    overtime_pay = (pay_rate * 1.5) * overtime
else: overtime_pay = 0.0

if overtime > 0.0:
    reghours = work_hours - overtime
else: reghours = work_hours

reghourpay = reghours * pay_rate
gross = reghourpay + overtime_pay
print("-----------------------------------")
print(f'Employee name:   {name}')
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("-----------------------------------------------------------------------------------")
print(f'{work_hours:.1f}           ${pay_rate:.1f}      {overtime:.1f}        ${overtime_pay:.2f}         ${reghourpay:.2f}       ${gross:.2f}')


