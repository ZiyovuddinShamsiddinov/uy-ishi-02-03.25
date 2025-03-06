import re
from django import forms
from django.core.exceptions import ValidationError
from .models import Student,Subject
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('full_name', 'phone', 'location', 'subject')
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'subject': forms.Select(attrs={'class': 'form-control'}),
        }

class SubjectsForm(forms.ModelForm):

    class Meta:
        model=Subject
        #fields='__all__'
        fields=['title']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
        }