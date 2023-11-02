'''
When an object is erased or destroyed in Object oriented programming, a destrcutor is invoked.
A constructor (__init__) is automatically called when you create an object in Python.
A destructor is called automatically whenever an object is deleted using del function or there are no more references
of the object or program eds.

Syntax:

def __del__(self):
    # body of destructor

whenever python sees this method, It automatically deletes and clears all the references to the object.
'''


class Computer:
    def __init__(self):
        self.name = "Computer"

    def __del__(self):
        print('destructor called')


c = Computer()
print("Computer")

# print("Computer")
print(c)

# def func():
#     c = Computer()
#
#
# func()
# print("Computer")


'''
In Python, a destructor is a special method called __del__ that is used to clean up resources or perform any necessary 
cleanup operations when an object is about to be destroyed or deallocated. It's not commonly used because Python has a 
garbage collector that automatically reclaims memory and resources when objects are no longer in use. However, in some 
cases, you may want to define a destructor to ensure that specific cleanup tasks are performed.

Here's a detailed explanation of Python destructors and an example usage:

Destructor Method:
The destructor method is defined as __del__ within a class.
It's automatically called when the object is about to be destroyed.
You can use the __del__ method to release resources like closing files, releasing network connections, or any other 
cleanup tasks.

Usage and Best Practices:
Destructors are not commonly used in Python because the built-in garbage collector efficiently manages memory and 
resources. It's recommended to rely on context managers (using the with statement) for resource cleanup, as it ensures 
that resources are properly released, and the code is more readable.

Here's an example of a destructor:
'''


class FileHandler:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def open_file(self):
        self.file = open(self.filename, 'w')
        return f"File {self.filename} opened."

    def write_to_file(self, data):
        if self.file:
            self.file.write(data)
            return f"Data written to {self.filename}."
        else:
            return "File not open."

    def __del__(self):
        if self.file:
            self.file.close()
            print(f"File {self.filename} closed in destructor.")


# Create a FileHandler instance
file_handler = FileHandler("example.txt")

# Open the file
print(file_handler.open_file())  # Output: File example.txt opened

# Write data to the file
print(file_handler.write_to_file("Hello, World!"))  # Output: Data written to example.txt.

# At this point, the object is still in use, and the destructor is not called.

# When the object is about to be destroyed, the destructor is automatically called.
# This will close the file and display the message.
del file_handler  # Output: File example.txt closed in destructor.

'''
In the example, we define a FileHandler class with an __init__ method for creating an instance, an open_file method to 
open a file for writing, and a write_to_file method to write data to the file. The __del__ method is defined to 
automatically close the file when the object is about to be destroyed. When we delete the file_handler object, 
the destructor is called, closing the file and displaying a message.

However, it's important to note that relying on the destructor for resource cleanup is not a best practice in Python. 
It's better to use context managers (with statements) or explicitly close resources when they are no longer needed, 
as it provides more control and clarity in your code.'''
