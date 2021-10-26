"""Discussion_Forum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from forum import views

#in url patterns we are defining names because we will able to call them with "{% url 'name' %}" in the html
urlpatterns = [
    path('admin/', admin.site.urls),
    #path("", views.forum, name="Forum"),
    ##path("discussion/<int:myid>/", views.discussion, name="Discussions"),

    path("", views.home, name="home"),
    path("register/", views.registerpage, name="register"), 
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),

    ##path("logout/", views.UserLogout, name="Logout"),
    ##path("myprofile/", views.myprofile, name="Myprofile"),
]
