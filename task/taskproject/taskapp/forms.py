from django import forms
from .models import Data
class Data_form(forms.ModelForm):
    class Meta:
        model=Data
        fields=['name','date_of_birth','age','gender','phone','mail','address','department','purposes']

        