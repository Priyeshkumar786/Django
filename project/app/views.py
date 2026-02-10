from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import redirect 
# Create your views here.

def home(req):

    # return HttpResponse("my first django project")


    # plain_text
    # return HttpResponse("this is plain text",content_type="text/plain")

    # html
    # html="<h1>this is myt first django project</h1><p>welcome to IT</p>"
    # return HttpResponse(html,content_type="text/html")


    # json_data
    import json

    data={"name":"priyesh","role":"developer","active1":True,"active2":False}
    json_data=json.dumps(data)
    return HttpResponse(json_data,content_type="application/json")




# def home1(req,name):
#     return HttpResponse(f'hello {name} this is cybrom')

# def home2(req,pk):
#     x=pk*10
#     return HttpResponse(f'{x}')


# def home3(req,pk):
#     x=pk,10
#     return HttpResponse(f'{x}')


# def home4(req,pk):

#     return HttpResponse(f' hello {pk}')

# def home5(req):
#     data = {'name':'neeraj','email':'mishrapriyesh.521@gamil.com'}
#     # return render(req,'home.html',{'data':data})

#     # return render(req,'home.html')


# # def home6(req):
#     return redirect('https://divineyatra.vercel.app/')


# --------------------------------------------------------------------
# ===============================URL to URL==============================


# def priyesh(req):
#     return redirect('prabhat')

# def priyesh123(req):
#     return HttpResponse("hello.....")

# def new123(req):
#     return render(req,'home.html')

def priyesh1(req):
    return redirect('taresh123')

# =====================HW make landing page by django

# json_data
    import json
        data={"name":"priyesh","role":"developer","active1":True,"active2":False}


