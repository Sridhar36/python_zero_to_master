from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # '' represents home page
    # here we are saying, hey if you are looking for homepage go find in views.home i.e., home function in views

    path('add', views.add, name='add')
    # add because once you enter values and click submit, you see url has add in it
]
