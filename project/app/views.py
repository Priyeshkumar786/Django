from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(req):
#     return HttpResponse("my first django project")

# def home1(req,name):
#     return HttpResponse(f'hello {name} this is cybrom')

# def home2(req,pk):
#     x=pk*10
#     return HttpResponse(f'{x}')


# def home3(req,pk):
#     x=pk*10
#     return HttpResponse(f'{x}')


def home4(req,pk):
    # return HttpResponse(f'{x}')
    return HttpResponse("this is plain text response.",content_type="text/plain")



