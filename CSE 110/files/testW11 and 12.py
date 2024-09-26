#strip - cleaning a string
# sentence = " This has a leading space and trailing too "
# print(f"'{sentence.strip()}'")
# print(f"'{sentence}'")
# sentence = sentence.strip()
# print(sentence)
# split - get multiple 
# sentence = "This is a sentence# to be split"
# parts = sentence.split('#')
# for part in parts:
#     print(part.strip())

#Files
#file = open('data.txt')
#file.close()
min_rating = 99
min_title= ''
max_rating = 0
max_title = ''
with open('files/data.csv') as file:
    file.readline()
    for line in file:
        parts = line.split(',')
        title = parts[0]
        rating = int(parts[1])
        print(f'{title} - ({rating})')
        
        if rating < min_rating:
            min_rating = rating
            min_title = title
        
        if rating > max_rating:
            max_rating = rating
            max_title = title

print(f'Worst movie in the list is {min_title} with a rating of {min_rating}')
print(f'Best movie in the list is {max_title} with a rating of {max_rating}')