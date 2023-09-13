from django import forms
from .models import Eventappli

class Eventappliform(forms.ModelForm):
    class Meta:
        model =Eventappli
        fields = ['full_name','email','phone']

