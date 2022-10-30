'''
udemy link - https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16077440#overview

In my words - encapsulation is binding data and functions {i.e.,attributes and methods}  together & encapsulate into
one big object so that we keep everything in this capsule or blue-print. We can create multiple objects out of this
blue-print.

Encapsulation is the binding of data and functions that manipulate that data.And we encapsulate into one big object so
that we keep everything in this box that users or code or another machines can interact with.
And this data and functions are what we call attributes and methods.

below:
We're able to encapsulate the functionality of our player character by having name and age data or attributes and
also have functions that can act upon this name and age.

I'm encapsulating the functionality.
If I didn't have this class, I would have, well, some variables and then two functions.
But by using encapsulation, I've packaged this up into a blueprint that I can create multiple objects
of, so that when other people see my code, they know, Hey, this is an entire object that I can interact
with. I can use in certain ways that player character describes.

And we've also seen this in our built-in Python data types, right? When I create a string.
Because of encapsulation, I have all this functionality available to me, all these methods that I
can access so that if I do, let's say capitalize, it will capitalize all my strengths.
I have all this functionality encapsulated for me to use.

Now.

Why do we want to package data and functions into attributes and methods?
Well, because this gives us extra power, right?
If, for example, this player character doesn't have any actions, any methods and just had attributes.
Well, in that case, this is kind of like a dictionary, right?
It's kind of useless if I print player one here and I click run.
I have this player object but I can access name like this.And I can also access age.

But I can't really do anything to it.I could have the same dictionary here.
Let's say player two that is going to equal a dictionary that has name of Andre and then age of 100.

And the only real difference between the two is the way I access this information.
Instead of the dot notation, I use the bracket notation to access the keys.So that when I click Run.

I have to make sure that I do two here for player two.If I click Run.Again.It's the same thing.
Sure I can do it this way, but it's kind of useless.
Why not just create a dictionary if all I want is data?

But using this way, I'm combining things, packaging things up into those instances, into those boxes
that can be useful and also things that have meaning.Right?
Because our world is full of data and actions, right?
Even a tree, for example, if we had a tree class in our real world, the tree would have maybe whether
it was an evergreen or a perennial, it will have whether it has lease or it doesn't, how tall it is.
We'll have all that information, but also actions.Right?

I can cut down a tree.The tree can grow, the tree can extend its roots.
So this way we're able to mimic what happens in the real world with our code.
So that is encapsulation and we've seen it.
'''


class PlayerCharacter():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run!!")

    def speak(self):
        print(f'my name is {self.name}, and I am {self.age} years old')


player1 = PlayerCharacter('andrei', 100)
player1.speak()  # this is abstraction in action. We need not know how this speak() method is built.

'''
Abstraction: abstraction means hiding of information or abstracting away information and giving access to only what's 
necessary. So whatever the user or the programmer or the machine is interested in, that's the only thing we give

The idea is to abstract away this code, and although it can be modified and overridden by using these
proper conventions like private attributes, we're able to abstract things away, but still make sure
that whatever the user might be using isn't going to break our code.
'''

# abstraction eg2:
print(len((1, 2, 3, 4, 5)))  # here this prints length of the tuple.
'''
If I do length here and I click run. I get a length of four, but I don't really need to know how length was implemented
in Python. It's abstracted away from us.I get a length of four, but I don't really need to know how length was 
implemented in Python. It's abstracted away from us.And this is the power of OP.

It abstracts away things that we don't need to care about, or at least it makes us more efficient so that we know that 
it works a certain way and we're not wasting our time learning or coding from scratch. If we had our iPhone, for example
well, the camera feature on an iPhone, it'll be nice for an app that we build to use it, but we don't need to actually 
know exactly how the iPhone camera is coated on an iPhone note.Instead, the iPhone usually gives us a way to say Camera,
dot, take. Picture. To actually allow us to take a picture without knowing how the Apple engineers actually coded the 
camera. So it's a very powerful concept.
'''

Player2 = PlayerCharacter('andrei', 100)
Player2.name = '!!!!'
Player2.speak = 'BOOO'
print(Player2.speak)

'''
So you're thinking, I think I'll get abstraction. But let me ask you this. Could I just do player one.Dot name equals to
let's say, exclamation marks and then player dot run. Or you know what? Let's do speak equals to boo. Make sure it's 
player one.Well, if I now print and do player one. Dot speak and I tried to run this function.Let's see.
I get string object is not callable because speak has been modified.
Speak has been modified to a string value instead of this actual function that we would have needed.
So that if I run just checking the speak attribute I get boo.I mean, abstraction is good, but hold on a second here.

This is bad.
If I have a class that I've abstracted away, but anybody can come along.
Any programmer can come along and just remove all my hard work and overwrite it like that.
Isn't that bad?

That is, we over wrote name and speak.
And now all that hard work that we put into our class has been overridden by this.
I mean, sure, if we instantiate a new object. We will have our run and speak, but player one now is completely useless.

It has no name and speak.
It just says Boo.
Completely useless.

Now in Python, there's this idea of 'public and private', and this is related to our discussion of abstraction.

The idea behind abstraction is that we hide away information and only give access to things that a user is concerned about.
Right.
So ideally, we shouldn't have access to init.

But in Python, there's no true privacy, no true private variables.So how do we get around this?
Well, what we would do is do underscore variable name.
---------------------------------------------------------------------
there's no true private variables in Python.
As programmers, we've decided that underscore means that you shouldn't touch this. Please don't touch this.
You can still be bad and do something like this.
But I'm letting you know ahead of time if you see underscore this shouldn't be modified, this should be private.
And that's how we achieve privacy in Python. We all kind of agreed to say, hey, let's keep this little thing private.
So if you ever want to keep a method or a an attribute private, you just put an underscore in front of it, but it's no 
guarantee.

__ (dunder methods):  this double underscore is also a convention to let people know you shouldn't really touch this or modify this with
each data type.
'''
