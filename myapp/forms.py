from django import forms
from . models import Table

class TableForm(forms.ModelForm):
    class Meta:
        model=Table
        fields=['first_name','last_name','email','address']