from django.shortcuts import render, redirect, HttpResponse, Http404
from django.forms import inlineformset_factory
#from django.contrib.auth.forms import UserCreationForm # I commented this because I created costumized form from forms.py
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import  messages
from django.contrib.auth.decorators import login_required # it is basically for login required for accessing home page
from django.contrib.auth.models import User
#for posts
from .models import Post, Profile


def registerpage(request):

    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            password1 = form.data.get('password1')
            password2 = form.data.get('password2')
            username = form.data.get('username')
            print(password1,password2,username)
            if form.is_valid():
                context = {"form": form}
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,"Account created for"+ user)
                return redirect("login")

            elif len(password1)<8:
                messages.error(request,"Password should be longer then 8 digits")
                context = {"form": form}
                return render(request,"register.html",context)

            elif password1 != password2:
                messages.error(request,"Password doesn't match!")
                context = {"form": form}
                return render(request,"register.html",context)

            elif not username.isalnum():
                messages.error(request,"Username must contain only letters and numbers!")
                context = {"form": form}
                return render(request,"register.html",context)

        else:
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
            
    context = {} #just creating for further possible data/dictionary
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login') #if a person not login this redirecting to login page
def home(request):
    profile = Profile.objects.all()

    if request.method == "POST":
        if 'entry' in request.POST:    
            user = request.user
            content = request.POST.get("content","")
            #taking user data from Post class
            post = Post(user2 = user, post_content = content,likes = 0)
            post.save()
            alert = True #creating alert for limitations
            context = {'alert':alert}
            return render(request,"home.html",context)
        
        elif "edit" in request.POST:
 
            user = request.user
            #getting post_id for editing
            post_id_ =request.POST.get('edit','')
            
            content = request.POST.get("content-edit-"+str(post_id_),"")
            
            post = Post.objects.get(pk = post_id_)
            post.post_content = content
            
            post.save()
            
            alert = True
            context = {'alert':alert}
 
            return render(request,"home.html",context)

        elif "delete" in request.POST:
            post_id_ =request.POST.get('delete','')
            post = Post.objects.get(pk = post_id_)
            post.delete()
            alert = True
            context = {'alert':alert}
            return render(request,"home.html",context)

        elif "like" in request.POST:
            post_id_ =request.POST.get('like','')
            post = Post.objects.get(pk = post_id_)
            post.likes = int(post.likes)+1
            post.save()

            alert = True
            context = {'alert':alert}
            return render(request,"home.html",context)
    
    posts = Post.objects.filter().order_by('-timestamp') #ordering post by timestamp
    context1 = {'posts':posts}
    return render(request,"home.html",context1)




