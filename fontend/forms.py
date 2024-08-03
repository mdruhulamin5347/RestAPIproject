from django import forms
from home.models import contactserializer
from django.contrib.auth import get_user_model
class contactForm(forms.ModelForm):
    class Meta:
        model = contactserializer
        fields = '__all__'
    

user_model = get_user_model()
class loginform(forms.ModelForm):
    class Meta:
        model = user_model
        fields = ['username','password',]