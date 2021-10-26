from django.shortcuts import render, redirect, HttpResponse, Http404
from django.forms import inlineformset_factory
#from django.contrib.auth.forms import UserCreationForm # I commented this because I created costumized form from forms.py
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages
from django.contrib.auth.decorators import login_required # it is basically for login required for accessing home page



def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Account created for"+ user)

                return redirect("login")



        context = {"form": form}
        return render(request,"register.html",context)

def loginPage(request):

    if request.method == "POST":
        #I amauthenticating here
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
    #here I am checking user exist or not
        if user is not None:
            login(request,user)
            return redirect("home")

        else:
            messages.info(request,'Password or Username is incorrect')
            
    context = {}
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login') #if a person not login this redirecting to login page
def home(request):

    context = {}
    return render(request,"home.html",context)


