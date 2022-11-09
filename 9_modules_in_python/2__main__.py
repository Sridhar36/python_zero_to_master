'''
if we run a module in python:
python interpreter first runs all the imported modules first and stores in memory i.e pycache. Then it starts executing
the actual module. It adds the modules to  memory because we are going to use those methods that are present in the
imported module.

So it is better always to import only what is needed.

to check : we can do print(__main__)
'''

# if __name__ = '__main__':

'''if we want to run some code only in the main file, then we can use if __name__ = '__main__': 
to check if it is only the main class that is run then only  execute something.
'''
