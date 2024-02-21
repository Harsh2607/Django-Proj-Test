from django import forms
# built-in validators for django
from django.core import validators  
from Django_App_01.models import Album, Musician, Post, UserProfileInfo
from django.contrib.auth.models import User


# custom validation to check if name starts with 'a'
def check_name(value):
    if value[0].lower() != "a":
        raise forms.ValidationError("Name should start with letter 'a'")

class InputForm(forms.Form):
    user_name = forms.CharField(validators=[check_name])
    user_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    
    # Manual bot checking
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput)
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data["botcatcher"]
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

    # Validation using Django built-in validators
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

class NewForm(forms.ModelForm):
    class Meta():
        model = Album
        fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ("username", "email", "password")

class UserProfileInfoForm(forms.ModelForm):
    portfolio = forms.URLField(required=False)
    picture = forms.ImageField(required=False)
    class Meta:
        model = UserProfileInfo
        exclude = ["user"]