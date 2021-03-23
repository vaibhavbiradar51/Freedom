from django import forms  
from .models import  Log
  
class LogForm(forms.ModelForm):  
    class Meta:  
        model = Log
        fields = ['idNumber']
class LogoutForm(forms.Form):
    id_number = forms.CharField(max_length=15)