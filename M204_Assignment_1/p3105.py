'''
Q.3. Write a Python program which prompts the user to input temperature in Celsius, convert the
temperature to Fahrenheit and display both the values with appropriate titles. Use the following
formular: T(°F) = T(°C)× 9/5 + 32
'''

#temperature
celcius = float(input('Enter Temperature in Celcius : '))
farenheit = celcius * (9/5) + 32
print('Temparature : ')
print('Cencius : ',celcius)
print('Farenheit : ',farenheit)
