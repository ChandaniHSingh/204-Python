'''
Q.1. Write a Python program to input principal amount, rate of interest and number of years with
appropriate prompts. Find simple interest and display all the details in the following format:
Principal Amount : Rs. __________
Rate of Interest : ____ %
Number of Years : ____
Simple Interest : Rs. __________
Maturity Amount : Rs. __________

'''
#Simple Interest

principalAmount = float(input('Enter Principal Amount : '))
rateOfInterest = float(input('Enter Rate of Interrest : '))
numberOfYears = float(input('Enter Number of years : '))
simpleInterest = (principalAmount * rateOfInterest * numberOfYears) / 100
maturityAmount = principalAmount + simpleInterest

print('Principal Amount : Rs. ',principalAmount)
print('rate of Interest : Rs. ',rateOfInterest,'%')
print('Number of years : Rs. ',numberOfYears)
print('Simple Interrest : Rs. ',simpleInterest)
print('Maturity Amount : Rs. ',maturityAmount)
