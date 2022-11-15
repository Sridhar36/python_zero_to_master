'''
what is web server?  why you need web server? how to build one using Python?

what we've done with index.html is we've served to the browser some files from, as you can see, from our computer.
So all it's doing is the browser saying, hey, I'm going to display these files that are located right here on your
computer. So essentially we have a web server that's also running a browser, but that's not how real life works.
Why would that be? Well, imagine if you had your own website. Do you really want to have people from all over the world
access your website directly through your computer, grabbing the files from your computer? I mean, no. Right.
There's a lot of security issues. There's a lot of issues with performance. You have to keep your laptop on the entire
time so people can access your website. Instead, we want a web server which, as the name suggests, serves files and
specializes in serving files to browsers. Somewhere in the world that I don't have to worry about. It's not on my
computer. Somebody owns that machine, somebody owns that computer, and it's on all the time so that whenever
we go to a website or a link, it's always going to be running and sending those files out. So we're finally going to get
back to Python here because what we want to do is do something more sophisticated than just having these files on our
machine. Instead, we want to build a real server using Python that we can deploy so that people can access our
website anywhere in the world. So we're finally going to get back to Python here because what we want to do is do
something more sophisticated than just having these files on our machine. Instead, we want to build a real server using
Python that we can deploy so that people can access our website anywhere in the world. Now you might still be confused.
This whole process might not make complete sense to you because we're just getting started. But don't worry, by the end
of it all, it's all going to make sense. So let's forget about the browser for now and get into building a real server,
something more sophisticated than what we've done up until now, which is just a folder with these three files and we
just double click on index.html.
'''

'''
Python seems to have an HTTP server. - https://docs.python.org/3/library/http.server.html not much secure
Awesome. And this module actually allows us to create a server. You can see over here that all we need to do is use the 
HTTP server and well, we have ourselves a server
'''

'''
flask vs Django
A HTTP server is not recommended for production.

It only implements basic security checks. You see building servers? Is a very, very common thing.
A lot of Python developers are hired as backend engineers to build things like servers.
So when we use something like the HTTP server that's built in as part of the Python standard library,
well, we're redoing all these things that, frankly, a lot of developers have done before.
And when you have a problem that is constantly getting solved or the problem is constantly being rewritten
and rewritten and rewritten, we start to have something called libraries, but also something called
frameworks. And that is, instead of using something that, well, frankly, would take us a really long time to do.
And as you can see here, there's still a lot of issues like security issues that we need to check and fix.
We can use a framework like FLASK to build a server because so many engineers are building servers using Python.
Flask is a tool that uses perhaps underneath the hood something like HTTP server, but instead make  sure that the 
security, the added tools and benefits are already pre-built for us. You can think of it as a kitchen.
You're trying to bake a cake, and instead of you having to go by the knife, go by the bowl, the mixer,
the oven, go by the ingredients, all that stuff. Flask is like the kitchen where you get to enter the kitchen.
You have all the tools necessary, you have the ingredients, and all you have to do is cook. Now, when it comes to Python
there's two really popular frameworks. There's the FLASK framework and the Django framework. Right over here.
Now, Django is one of those frameworks that it's really, really big. It's a big, big kitchen. On the other hand, Flask 
is what we call a micro framework. That is it's extremely lean. It's a small library so that we can do things fast.
I'm going to teach Flask over the next couple of videos because I like the simplicity of it all.
Sometimes when you write in Django, it feels like you're not even writing Python because there are
so many rules and so many tools that you can use versus with flask. Everything is clean and small and it's great for our 
use. So how do we get started?'''

'''
1. to create a new venv: https://www.udemy.com/course/complete-python-developer-zero-to-mastery/learn/lecture/16283274#notes
python3 -m venv venvname

this creates the venv wherever console is in.
or
If you want to create venv in your own directory then do a cd and use command
or
you can make dir using mkdir <dir name> command

2. activate the env once created. We can use the script.exe under scripts

get into project directory and then do -> Scripts\activate.ps1

**if you get this error
Scripts\activate.ps1 : File C:\Users\sridh\PycharmProjects\pythonProject\pythonProject\webserver\Scripts\Activate.ps1 
cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at
https:/go.microsoft.com/fwlink/?LinkID=135170.

open powershell and run this command ->  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted


3. pip install flask


https://flask.palletsprojects.com/en/2.0.x/quickstart/
'''
