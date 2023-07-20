from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

#create admin
class CreateAdminForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email','password1', 'password2']

#register a user
class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2',]

class OrderForm(forms.ModelForm): 
    class Meta:
        model = models.OrderItem
        fields = ['product','order','quantity']

class ComplaintForm(forms.ModelForm):
    class Meta:
        model=models.Complaint
        fields=['description']
        widgets = {
        'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }
