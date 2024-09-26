import math
# ALL_length = float (input ('Enter a length value? '))
# print (f'The Area of square is: {str( ALL_length**2)}')
# print (f'The Area of a cube is: {str( ALL_length**3)}')
# print (f'The Area of a circle would be is: {round( math.pi * ALL_length, 0)}')
# print (f'The Area of a Sphere would be is: {round( 4 / 3 * math.pi * ALL_length**3, 0)}')

Square_length = float(input ('What is the length of a side of the square? '))
Rectangle_length = float(input ('What is the length of the rectangle? '))
Rectangle_width = float(input ('What is the width of the rectangle? '))
Circle_radius = float (input ('What is the radius of the circle?'))

print (f'The area of the Square is: {str (Square_length **2)}')
print (f'The area of the Rectangle is:{str( Rectangle_length * Rectangle_width)}')
print (f'The area of the circle is: {str( math.pi * Circle_radius**2)}')