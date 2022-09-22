


#This program caculates travel expenses and howmuch of your budget you'll have afterwords
#22/9/22
#CTI-110 P1HW2 - Travel Expense
#Ty McConnaughey
#
#------------------------------------------------------------------------------------------
#Display "This program calculates and displays travel expenses"
#Input for budget display "Enter Budget:"
#Input for destination display "Enter your travel destination:"
#Input for gas price display "How much do you think you will spend on gas?"
#Input for hotel price display "Approximately, how much will you need for accomodation/hotel?"
#In put for food price display "Last, how much do you need for food?"
#display "------------Travel Expenses------------"
#display location
#display budget
#display Fuel: price, Accomodation: price, and Food: price
#display Remaining Balance:
print('This program calculates and displays travel expenses')
budget=float(input('Enter Budget:'))
location=input('Enter your travel destination:')
gas=float(input('How much do you think you will spend on gas?'))
hotel=float(input('Approximately, how much will you need for accomodation/hotel?'))
food=float(input('Last, how much do you need for food?'))
print('------------Travel Expenses------------')
print('Location:', location)
print('Initial Budget:', budget)
print('')
print('Fuel', gas)
print('Accomodation:', hotel)
print('Food', food)
print('')
remainingBalance=budget-(gas+hotel+food)
print('Remaining Balance:', remainingBalance)
