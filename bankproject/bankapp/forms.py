from .models import District,Branch,Person
from django import forms
class regform(forms.ModelForm):
    class Meta:
        model = District
        fields = ['name']


