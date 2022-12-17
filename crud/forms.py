from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    model = Student
    fields = '__all__'