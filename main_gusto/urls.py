from django.urls import path
from .views import main,test

urlpatterns = [
    path('', main, name='main'),
    path('test', test)
]