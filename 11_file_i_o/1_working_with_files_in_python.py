file_path = 'C:\\Users\\sridh\\PycharmProjects\\pythonProject\\pythonProject\\zero_to_master_complete_python_2022\\11_file_i_o\\test_file'
myfile = open(file_path)
print(myfile.read())
print(myfile.read())  # this will not print anything, since the cursor is at the end there is nothing to print.

'''
But by the end of this first reading, the cursor is going to be at the end of the file. So now when it tries to read, 
it's going to be end of the file and nothing will be left there. So the way we get around this is to do something like 
this. We simply say my file dot C, which moves our cursor to whatever index we want. In our case, seek zero. So if I run
this now, there you go. And if I move the cursor back.'''

myfile.seek(0)  # takes cursor to 0 index
print(myfile.read())
myfile.seek(0)
# to read line by line
print(myfile.readline())
print(myfile.readline())
print(myfile.readline())

myfile.seek(0)
# to read all lines and store in list line by line
print(myfile.readlines())

myfile.close()  # to close the file
