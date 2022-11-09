'''
Each .py file in python is a module.

In real life, this isn't the case. We have a lot more code and we can't just have one file with millions line of code.
So how do we stay organized? Well. If we had multiple files of Python. Like this because our project is getting bigger
and bigger.
Would this work?
Is there a way for us to link all of these files together?

As a matter of fact, there is and this is very common practice all across industry, and we call this
way of organizing code modules. And modules are simply, well, these files.
Each one of these files, each dot pi file is a module.
And by building these modules, kind of like we built different functions, kind of like we built different
classes because inside of these files we can have classes, we can have functions, but we can also have different files.
So a layer higher to divide up our code.


Now, there's a few things that happened here when you import and run main class.
One is that we generated this py cache folder underscore, underscore, py cache.
This is this is pretty confusing, right? Well, this py cache is created every time we run a file with, let's say, import
 statements. So when we're using modules. You see, what Py Cash does is when we click Run.
The Interpreter is going to create this podcast folder and it's going to say, Hey, I'm running this
file, this one main py file, anything that may not py file imports, let's say utility.
In our case I'm going to cash it. So see how here it says dot py.

See this is because it's using the C Python interpreter.

Remember, this is the C python which is the interpreter written and C, so this is actually a compiled
file so that next time I click run here on my main pi, nothing changes because what's going to happen
is instead of loading up utility pi, it's going to load up this compiled version of utility because nothing has changed.
And utility py. And this makes things faster. When I tried to run Main Py again, that's what caching is. Caching is, hey
I'm going to remember this and this is the compile version so I don't have to go through the compilation step again.
But notice that the main pi file does not get compiled because, well, we run it every time.
Now, if we change the utility function to not have the divide in there, I click run and you don't
notice it here. But this has now been rerun because we have a different file. You see that we have multiply here but not
divide. So let's bring back divide again. Go back to here, click run. And there you go. We have divide here, too, now.
But this is something that we don't touch. This just comes underneath the hood with any editor that we use.
And in a few videos, we're going to show you how this also happens when we use something like pie chart.
This is just something that editors allow us to do just so our programs can run faster.
'''

# to import a module just give the import command and give module name

'''
A package is folder containing modules
to import - import pacakgename.modulename
'''

# everytime you import something and run your module.. there will be a cache folder that gets created.

'''
One of the rules of a package of a python package is that on the root of this package, you have to __init__ .py file
Now. Why is that? Well, because the interpreter is going to read this and say, oh, this is a Python package.
Remember how when I right clicked here, I said new and then I had an option of a directory or a python package.
By clicking python package, it automatically added this in it for us.So although here everything worked without a init, 
this is just something that other code editors  hides underneath the hood. Any time you want to create a package,
you'll see that we need to have an init file and it can just be completely empty.
Now the beauty here with pycharm is that it does it for you, which is really, really nice.'''

'''to access package inside package
import packagename.packagename.class
or 
from packagename.packagename import class
'''
