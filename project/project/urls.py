"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    #static url:-

    # path('admin/', admin.site.urls),
    path('home/',views.home),

    # path('app/',views.home),
    #dynamic url:-
    
    # path('home1/',views.home1,{'name':'priyesh'}),
    # path('home2/<int:pk>/',views.home2),                      
    # path('home3/<str:pk>/',views.home3),
    # path('home4/<slug:pk>/',views.home4),
    # path('home5/',views.home5),
    path('taresh/',views.priyesh),
    path('taresh123/',views.priyesh123,name='prabhat'),
    path('',views.new123),
  

]
