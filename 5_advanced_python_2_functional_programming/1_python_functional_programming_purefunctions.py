'''
We remember in our object oriented programming section how we had two classes to divide up attributes
and methods of, let's say, a wizard class and an Archer class.
And functional programming has this idea as well of separating concerns, but they also separate data and functions.
That's how a functional programmer views the world. Instead of combining methods and attributes, we separate them up
because there are two separate things. There's data and this data gets interacted and acted upon.
But we're not going to combine both data and functions as one piece in an object like we saw with object
oriented programming. Now there is no correct definition for what is and isn't functional.
But generally functional languages have an emphasis on simplicity, where data and functions are concerned,
because in most functional programming paradigms we don't have this idea of classes and objects.
Instead, functions operate on well defined data structures like lists and dictionaries that we saw
rather than belonging that data structure to an object.
But at the end of the day, the goal of a functional programming paradigm is the same as object oriented paradigm.
It's the idea of making our code clean and understandable, easy to extend.


Pure functions: Now a pure function has two rules.
One is that given the same input, it will always return the same output.
And the second point is this idea of a function should not produce any side effects.What are side effects?
Side effects are things that a function does that affects the outside world.
For example, if I was to print something inside of this function, it affects the outside world, right?
Because I'm printing something onto a screen.The screen is the outside world.
Or for example, if this function was touching a variable that lived outside of a different scope,that's a side effect.

'''


def multiply_by2(li):
    emplist = []
    for item in li:
        emplist.append(item * 2)
    # print(emplist) - now this is side effect for this function as it is dependent on print, which is outside world
    # entity for this function.
    return emplist


# no outside dependency for this function
# no matter how many times we run this function - it gives same output for the given same input
print(multiply_by2([1, 2, 3]))
