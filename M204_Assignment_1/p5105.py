'''
Q.5. Write a Python program to input principal amount and number of years with appropriate prompts. Find
simple interest and display all the details in the following format. Consider rate of interest based on the
following criteria. (NOTE: Use simple if..else statement to determine
the rate of interest)
Rate of interest = 5% if number of years < 1

= 5.5% if 1 <= number of years < 3
= 6 % if 3 <= number of years < 5
= 5.75% otherwise
Principal Amount : Rs. __________
Rate of Interest : ____ %
Number of Years : ____
Simple Interest : Rs. __________
Maturity Amount : Rs. __________
'''

#Simple Interest usig if..else

principalAmount = float(input('Enter Principal Amount : '))
numberOfYears = float(input('Enter Number of years : '))

if numberOfYears < 1:
    rateOfInterest = 5
elif numberOfYears >= 1 and numberOfYears < 3:
    rateOfInterest = 5.5
elif numberOfYears >= 3 and numberOfYears < 5:
    rateOfInterest = 6
else:
    rateOfInterest = 5.75

simpleInterest = (principalAmount * rateOfInterest * numberOfYears) / 100
maturityAmount = principalAmount + simpleInterest

print('Principal Amount : Rs. ',principalAmount)
print('rate of Interest : Rs. ',rateOfInterest,'%')
print('Number of years : Rs. ',numberOfYears)
print('Simple Interrest : Rs. ',simpleInterest)
print('Maturity Amount : Rs. ',maturityAmount)
