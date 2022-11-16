'''
Q.2. Write a Python program to find area of i) Square, ii) Rectangle, iii) Circle. Take input of all the values
need to calculate these areas from the user with appropriate prompts. Display all the values with
appropriate titles.
'''

#Square
length = float(input('Enter Lenght of Square : '))
area = length ** 2;
print('Area of Square : ',area)

#Rectangle
length = float(input('Enter Lenght of Rectangle : '))
width = float(input('Enter width of Rectangle : '))
area = length * width;
print('Area of Rectangle : ',area)

#Circle
radius = float(input('Enter Lenght of Circle : '))
area = 3.14 * (radius ** 2);
print('Area of Circle : ',area)
