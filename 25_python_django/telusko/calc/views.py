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
    val1 = request.GET['num1']
    val2 = request.GET['num2']
    res = int(val1) + int(val2)

    return render(request, 'result.html', {'result': res})
