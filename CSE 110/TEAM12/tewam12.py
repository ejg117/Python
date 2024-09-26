max_chapter=0
max_book=''
max_book_bom=''
max_chapter_bom=0
max_chapter_v=0
max_book_v=''
with open('TEAM12/books_and_chapters.txt') as file:
    file.readline()
    scripture_ask=input('Which volume of scripture would you like to learn about? ')
    for line in file:
        clean_line=line.strip()
        parts = clean_line.split(':')
        Book = parts[0]
        Chapter = int(parts[1])
        Scripture = parts[2]
        if Scripture == scripture_ask:
            if Chapter > max_chapter_v:
                max_chapter_v = Chapter
                max_book_v = Book
        if Scripture == 'Book of Mormon':
             if Chapter > max_chapter_bom:
                max_chapter_bom = Chapter
                max_book_bom = Book
        
             print(f'Scripture: {Scripture}, Book: {Book}, Chapter: {Chapter}')
            
        if Chapter > max_chapter:
             max_chapter = Chapter
             max_book = Book
        
    
print(f'The largest book with the most chapters is {max_book} with {max_chapter} chapters')
print(f'The largest book with the most chapters in the book of mormon is {max_book_bom} with {max_chapter_bom} chapters')
print(f'The volume {max_book_v} has {max_chapter_v} chapters')

