'''
Python has a built in email module and this module actually got updated with Python 3.6. So I'm going to show you the
latest version. When you Google how to send emails with Python, you might see a lot of outdated ways to send emails.
So just a heads up that you might see something different than what I'm about to show you.
But as of recording this video, this is the latest way to send emails. So why might this be useful?
Well, imagine you have a list of emails that you've collected and you want to launch a new startup.
You want people to know about your startup, right? So we can create a program that sends emails to maybe hundreds,
thousands of people at the same time, maybe a customized email with their name to promote our product. Now we'll get
into spamming and things like that later on. But you might be thinking to yourself, why do we need Python for this?For
example, there are tools like.MailChimp .Again, this is the email module that comes built in to Python.Now, SMTP is
going to allow us to create what we call an SMTP server. Any time you send emails to anybody, it needs to have a server
that communicates the language of the email.And this is what SMTP is used for. For example, on websites, you might see
HTTP or https as the protocol of communication between a browser and a server in the same way e mails have their own
protocol for communicating, and that's through SMTP.(simple mail transfer protocol. Gmail uses this, Hotmail uses this
pretty much most email clients.  I'm going to link to some resource if you want to read more about SMTP. But the key
thing is, if we want to send an email, we need SMTP server. Now from here, we're going to dive into how to send our
first email.
'''

import smtplib
from email.message import EmailMessage
