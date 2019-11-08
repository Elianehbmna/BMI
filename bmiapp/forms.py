from .models import Profile,Result
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['bio','profilepic'] 
        exclude=['user']   

class ResultForm(forms.ModelForm):
     class Meta:
         model=Result
         fields=['weight','height']
         exclude=['result']

