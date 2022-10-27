# You have to include folder even though this file is also in lib
# mode can be 'r', read-only, which is the default 
# (eg it will be read only if you don't include a mode), 
# or 'w' for write, or 'a' for append

with open('lib/test.txt', mode='r', encoding='utf-8') as text_read:
    #print(text_read.read())

    # to process one line at a time
    for line in text_read:
        print(line) #process line

# mode means reading mode, writing mode, etc
print (text_read.mode)
#r

text_read.close()

# in order to write

# The write and append modes will create a new file if it does not already exist. 

with open('lib/test.txt', mode='w', encoding='utf-8') as text_write:
    text_write.write('hello from file_io.py! :)\n')

# mode means reading mode, writing mode, etc
print (text_write.mode)
#w

text_write.close()

# in order to append

with open('lib/test.txt', mode='a', encoding='utf-8') as text_append:
    text_append.write(f'hello again from file_io.py :)\n')

# mode means reading mode, writing mode, etc
print (text_append.mode)
#w

text_append.close()

