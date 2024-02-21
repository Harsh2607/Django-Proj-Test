from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from Django_App_01.models import Musician, Album
from Django_App_01.forms import InputForm, NewForm, UserForm, UserProfileInfoForm
from django import forms

# Create your views here.
def index(req):
    # return HttpResponse("Hello World!")

    # dict1 = {"var1":"This is views.py file"}
    # return render(inputRequest, "Django_App_01\index2.html", context=release_date_dict)
    dict1 = {"text":"hello django", "value":100}

    return render(req, "Django_App_01/index2.html", context=dict1)

def albums(req):
    webpages_list = Album.objects.order_by("release_date")
    release_date_dict = {"albums":webpages_list}
    return render(req, "Django_App_01/albums_list.html", context=release_date_dict)

def input_form_view(req):
    f = InputForm()
    if req.method == "POST":
        f = InputForm(req.POST)
        if f.is_valid():
            print("Form Validation Success!")
            print("Name: " + f.cleaned_data["user_name"])
            print("Email: " + f.cleaned_data["user_email"])
            print("Text: " + f.cleaned_data["text"])
            
    return render(req, "Django_App_01/input_form.html", {"form":f})


def input_model_form(req):
    f= NewForm()
    if req.method == "POST":
        f = NewForm(req.POST)
        if f.is_valid():
            print("Validation Success!")
            f.save(commit=True) # save and commit the form in the database
            return index(req)   # return back to home page on submit button
        else:
            raise forms.ValidationError("FORM NOT VALID!")
    
    return render(req, "Django_App_01/input_model_form.html", {"form":f})

def user_register(req):
    registered = False
    
    if req.method == "POST":
        user_f = UserForm(data=req.POST)
        user_profile_f = UserProfileInfoForm(data=req.POST)
    
        if user_f.is_valid() and user_profile_f.is_valid():
            print("Validation Successful")
            user = user_f.save(commit=True)
            user.set_password(user.password)
            user.save()
            
            user_profile = user_profile_f.save(commit=False)
            # set one to one relation with user above to avoid collisions as done in class UserProfileInfo(models.Model) -> user = models.OneToOneField(User, on_delete=models.CASCADE)
            user_profile.user = user    # here, user means user_f from above
            if 'picture' in req.FILES:
                user_profile.picture = req.FILES['picture']

            user_profile.save()

            registered = True
        
        else:
            print(user_f.errors, user_profile_f.errors)
    
    else:
        user_f = UserForm()
        user_profile_f = UserProfileInfoForm()
    
    return render(req, "Django_App_01/registration.html", {"user_form":user_f, "user_profile_form":user_profile_f, "registered":registered})

def user_login(req):
    if req.method == "POST":
        username = req.POST.get('username')
        password = req.POST.get('password')

        user = authenticate(username=username, password=password)
    
        if user:
            if user.is_active:
                login(req, user)
                return HttpResponseRedirect(reverse("index"))
            
            else:
                return HttpResponse("Account Not Active!")
        
        else:
            print("Login Failed!")
            print(f"Username: {username}\n Password: {password}")
            return HttpResponse("Invalid Login Details!")
    
    else:
        return render(req, "Django_App_01/login.html", {})
    
@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse("index"))

@login_required
def user_login_message(req):
    return HttpResponse("Login Successful!!!")