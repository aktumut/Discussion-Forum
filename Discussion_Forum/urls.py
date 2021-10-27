
from django.contrib import admin
from django.urls import path
from forum import views

#in url patterns we are defining names because we will able to call them with "{% url 'name' %}" in the html
urlpatterns = [
    path('admin/', admin.site.urls),


    path("", views.home, name="home"),
    path("register/", views.registerpage, name="register"), 
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),


]
