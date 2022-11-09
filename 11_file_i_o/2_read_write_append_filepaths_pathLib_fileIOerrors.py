# standard way to read through a file
file_path = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\zero_to_master_complete_python_2022\\11_file_i_o\\test_file'

# r+ - read and write access - but whatever we write gets added from beginning i.e., index 0
# a - append mode - whatever we write to files gets added to the end.
# w - read write mode. Everytime files opens all the previous content will be gone. If the file is not there then it
# will create a new file.
with open(file_path, mode='r') as file:
    print(file.readlines())

# to create a file


'''
file paths - 

./ - refers current folder  
../ - two folders back
.../ - three folders back
'''

'''
path lib - Object oriented file system
useful when handling files using python
'''

'''
File IO errors:
One of the common patterns when working with files is to actually put them in a try except lock. So in here we can say 
try and actually put them. Like this and try out to see if the file exists so we can say Except.
'''

try:
    with open('file.txt', mode='r') as txt:
        print(txt.read())
except Exception as err:
    print(err) # prints [Errno 2] No such file or directory: 'file.txt'
    # if we want to raise it then raise err we can do
