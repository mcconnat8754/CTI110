# CTI-110
# P4HW2 - Salary Calculator
# Ty McConnaughey
# 11/22/22
#
# create variable to track number of loops
# create input fir name with the prompt "Enter employee's name or, "None", to terminate: "
# create loop that ends when "None" is entered
# do math for previously mentioned tracking variable
# make input for hours with prompt "How many hours did {name} worked?" 
# create input for pay rate with prompt "What is {name}'s pay rate?"
# print employee name
# calculate the overtime hours, overtime pay, regular pay, and gross pay for the employee and assign it all to a variable
# create a variable for the total overtime pay across all loops
# create a variable for the total regular pay across all loops
# create a variable for the total pay across all loops
# create statement that starts when the loop ends
# print "Total number of employees entered:" followed by the loop counting variable
# print "Total amount payed for overtime:" followed by total overtime pay variable
# print "Total amount payed for regular hours:" followed by total regular pay variable
# print "Total amount payed in gross:" followed by total pay variable
entered = 0
name = input("""Enter employee's name or, "None", to terminate: """)
while name != "None":
    entered = entered + 1
    hours = float(input(f'How many hours did {name} worked? '))
    payrate = float(input(f"What is {name}'s pay rate? "))
    print('')
    print(f'Employee name:    {name}')
    print('')
    #----------------math------------------------
    if hours > 40:
        overtime = hours - 40
        hours = hours - overtime
    else: overtime = 0
    if overtime > 0:
        overtime_pay = (payrate * 1.5) * overtime
    regpay = hours * payrate
    gross = regpay + overtime_pay
    if entered == 1:
        totaloverpay = overtime_pay
        totalreg = regpay
        totalgross = gross
    else:
        totaloverpay += overtime_pay
        totalreg += regpay
        totalgross += gross
    #--------------------------------------------
    print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
    print("--------------------------------------------------------------------------------")
    print(f'{hours:.1f}           ${payrate:.1f}      {overtime:.1f}        ${overtime_pay:.2f}         ${regpay:.2f}       ${gross:.2f}')
    print('')
    name = input("""Enter employee's name or, "None", to terminate: """)
else:
    print('')
    print(f'Total number of employees entered: {entered}')
    print(f'Total amount payed for overtime: ${totaloverpay:.2f}')
    print(f'Total amount payed for regular hours: ${totalreg:.2f}')
    print(f'Total amount payed in gross: ${totalgross:.2f}')
    
