Grade = float(input('What is your grade? '))
letter = ''
if Grade >=97:
    letter = ('A+')
elif Grade >92:
    letter = ("A")
elif Grade >=90:
    if Grade <=92:
        letter = ("A-")
elif Grade >=87:
    if Grade <=89:
        letter = ("B+")
elif Grade <=86:
    if  Grade >=83:
        letter = ("B")
elif Grade >=80:
    if  Grade <=82:
        letter = ("B-")
elif Grade <=79:
    if Grade >=77:
        letter = ("C+")
elif Grade <=76:
    if Grade >=73:
     letter = ("C")
elif Grade <=72:
    if Grade >=70:
     letter = ("C-")
elif Grade <=60:
     letter = ("F")
print (letter)
if Grade >= 70:
    print('You passed the class')
else:
    print('You failed the class')