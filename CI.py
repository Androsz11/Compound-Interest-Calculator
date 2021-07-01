# App: Compound Interest Calculator
# Developed Date: 29th June 2021
# Devloper: HMandro

import os
Loop = True
while Loop == True:
	os.system('cls' if os.name == 'nt' else 'clear')
	
	P = float(input('Enter the Principal Amount: '))
	R = float(input('Enter the interest rate per annum: '))
	N = float(input('Enter the number of years: '))

	Amount = P*(1+R/100)**N
	os.system('cls' if os.name == 'nt' else 'clear')
	
	Amount = int(Amount)
	Interest = int(Amount-P)
	
	print(f"Principal = ₹{P}")
	print(f"Rate of interest per annum = {R}%")
	print	(f"Number of years = {N}yrs") 
	print(f"Total Amount = ₹{Amount}")
	print(f"Total Interest = ₹{Interest}")
	
	Loop2 = True
	while Loop2 == True:
		Choice = input('\n\nDo you want to calculate again? (Y/n)')
	
		if Choice == 'Y' or Choice == 'y' or Choice == 'Yes' or Choice == 'yes':
			Loop2 = False
		elif Choice == 'N' or Choice == 'n' or Choice == 'No' or Choice == 'no':
			Loop = False
			Loop2 = False
		else:
			print("Wrong choice!")