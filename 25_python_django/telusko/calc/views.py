from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello World")
'''
Here in http response you can add your HTML code like <p>Hello World</p> etc.,
but dont you think that will create a mess here,. So  you can add your html files in project and call those files here.
Which will be a static content.

But if you want dynamic content, then you have something like templates in Django. Concept is called DTL.. 
Django Template Language.,

We can have HTML page and in that we have dynamic content. 


'''


def home(request):
    return render(request, 'home.html', {'name': 'SridharGoud'})


def add(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    operation = request.GET['operation']
    if operation == 'add':
        res = num1 + num2
    elif operation == 'subtract':
        res = num1 - num2
    elif operation == 'multiply':
        res = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        res = num1 / num2
    else:
        return "Error: Invalid operation."

    return render(request, 'result.html', {'result': res})


def calculate(request):
    num1 = request.GET['num1']
    num2 = request.GET['num2']
    operation = request.GET['operation']
    if operation == 'add':
        res = int(num1) + int(num2)
    elif operation == 'subtract':
        res = num1 - num2
    elif operation == 'multiply':
        res = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        res = num1 / num2
    else:
        return "Error: Invalid operation."

    return render(request, 'result.html', {'result': res})

# def sub(request):
