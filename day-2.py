print('welcome to the tip calculator')
bill=float(input('what was the total bill '))
tip=int(input('what percentage would you like to give ? '))
people=int(input('how many people to split the bill '))
total_bill=bill*(1+tip/100)
total_bill_per_pearson=total_bill/people
print(f'each person should pay: {total_bill_per_pearson}')