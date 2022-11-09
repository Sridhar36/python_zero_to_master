'''
If you want to become a senior programmer and long lasting career then make sure you understand the testing conecpts

Each main file will have a test file.

'''

import unittest
import main

'''
Now the way unit test works is we create a class and then name it whatever you want. And here we'll have all our tests.
So let's just call it Test Main.And we inherit inside of this class what unit test gives us, which is a test. So this is
just a standard way to work with unit test. So we're inheriting whatever unit test test cases and now we have that 
functionality available in our test main class. Now in here we can start testing and writing code to test.

unittest has various assert methods using which we can verify the results.

UNIT TEST framework:
Another default method that we get with unit test is something called set up. And set up. Allows us to run a piece of 
code. That sets up before each call of the test. So this is really, really useful. If you need to set up something 
before each function. Let's say you have some default variables maybe that you need to set up. Well, in that case, this 
is a very useful method. Another one just like setup.Usually you add. At the bottom of the file. And in here, this is 
called a tear down. And as the name suggests, we run it at the end of each method that we call. So in here, let's say 
cleaning up. And usually you do this to clean up some variables, maybe reset some variables. If I run this. You see that
I have now about to test the function. And then we're cleaning up for each one of these methods. So these two are very, 
very useful when setting up and tearing down tests. Now tear down. You won't use as often. Usually you use it if you're 
testing something more complicated, like a database.'''


class TestMain(unittest.TestCase):

    def setUp(self):
        print("\nThis method runs before each test method")

    # test method -1
    def test_do_stuff(self):
        print("method - 1")
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # unittest gives us these assert methods

    # test method 2
    def test_do_stuff2(self):
        print("method - 2")
        test_param = 'sdsdsdsds'
        result = main.do_stuff(test_param)
        # self.assertEqual(result, ValueError)
        '''
        The assertion error is coming from our test file over here, and I'm asserting that, hey, I want to make sure 
        that the result and the value error are equal. Now you see over here that there's a bit of a mismatch.We have a 
        value error over here doesn't equal the class value error. Now this is a bit of a trick where because we're 
        returning an error. It's actually an instance of the value error class.'''
        self.assertTrue(isinstance(result, ValueError))
        # or
        self.assertIsInstance(result, ValueError)

        '''
        So by using tests and as testing and breaking things, I was able to improve this function. So it's more durable 
        so that now it works a lot better in production.Right? And this is the power of tests. It allows us to check for
        any mistakes that we may have made because maybe we wouldn't have thought of doing something like this initially
        But by writing tests alongside our code, we were able to improve the function.'''

    # test method 3
    def test_do_stuff3(self):
        print("method - 3")
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    # test method 4
    def test_do_stuff4(self):
        print("method - 4")
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    def test_do_stuff5(self):
        print("method - 5")
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, "please enter a number")

    def tearDown(self):
        print("This method runs after each Test Method")


# The last block helps to run the test by running the file through the command line.
if __name__ == '__main__':
    unittest.main()

'''
excercise
'''