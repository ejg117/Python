import math

def compute_area_rectangle(length, width):

    return length * width


def compute_area_square(side):
    area = compute_area_rectangle(side, side)
    return side * side

def compute_area_circle(radius):
    
    return math.pi * radius * radius

def compute_area(shape, value1, value2=0):
    area= -1
    if shape == "square":
        area = compute_area_square(value1)
    elif shape == "circle":
        area = compute_area_circle(value1)
    elif shape == "rectangle":
        area = compute_area_rectangle(value1, value2)
    
    return area

shape = ''


while shape != 'quit':
    shape= input('What shape do you want? ')
    shape = shape.lower()
    if shape == 'square':
            side= float(input('What is the length of one side of the square? '))
            area=compute_area(shape, side)
            print(f'the area is {area: .2f}')
    elif shape == 'rectangle':
            length= float(input('What is the length of the rectangle? '))
            width= float(input('What is the width of the rectangle? '))
            area=compute_area(length, width)
            print(f'the area is {area: .2f}')
    elif shape == 'circle':
            radius= float(input('What is the radius of the circle? '))
            area=compute_area(radius)
            print(f'the area is {area: .2f}')



    