from django import forms
from .models import Data,Branch
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class Data_form(forms.ModelForm):
    class Meta:
        model=Data
        fields=['name','date_of_birth','age','gender','phone','mail','address','purposes','department','branch']

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['branch'].queryset = Branch.objects.none()

            if 'department' in self.data:
                try:
                    department_id = int(self.data.get('department'))
                    self.fields['branch'].queryset = Branch.objects.filter(department_id=department_id).order_by('name')
                except (ValueError, TypeError):
                    pass  # invalid input from the client; ignore and fallback to empty queryset
            elif self.instance.pk:

                self.fields['branch'].queryset = self.instance.department.branch_set.order_by('name')


    CHOICES = [('MALE', 'Male'),
                ('FEMALE', 'Female')]
    
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    date_of_birth = forms.DateTimeField(widget=forms.SelectDateWidget())







        