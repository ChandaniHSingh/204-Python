'''
Q.7. Attempt Q.5. using shorthand if..else. 
'''

#Simple Interest usig if..else

principalAmount = float(input('Enter Principal Amount : '))
numberOfYears = float(input('Enter Number of years : '))

rateOfInterest = 5 if numberOfYears<1 else 5.5 if numberOfYears>=1 and numberOfYears<3 else 6 if numberOfYears>=3 and numberOfYears<5 else 5.75

simpleInterest = (principalAmount * rateOfInterest * numberOfYears) / 100
maturityAmount = principalAmount + simpleInterest

print('Principal Amount : Rs. ',principalAmount)
print('rate of Interest : Rs. ',rateOfInterest,'%')
print('Number of years : Rs. ',numberOfYears)
print('Simple Interrest : Rs. ',simpleInterest)
print('Maturity Amount : Rs. ',maturityAmount)
