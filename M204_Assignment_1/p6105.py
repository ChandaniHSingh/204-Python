'''
Q.6. Attempt Q.5. using Nested if.
'''

#Simple Interest usig if..else

principalAmount = float(input('Enter Principal Amount : '))
numberOfYears = float(input('Enter Number of years : '))

if numberOfYears < 5:
    if numberOfYears < 3:
        if numberOfYears < 1:
            rateOfInterest = 5
        else:
            rateOfInterest = 5.5
    else:
        rateOfInterest = 6
else:
    rateOfInterest = 5.75

simpleInterest = (principalAmount * rateOfInterest * numberOfYears) / 100
maturityAmount = principalAmount + simpleInterest

print('Principal Amount : Rs. ',principalAmount)
print('rate of Interest : Rs. ',rateOfInterest)
print('Number of years : Rs. ',numberOfYears)
print('Simple Interrest : Rs. ',simpleInterest)
print('Maturity Amount : Rs. ',maturityAmount)
