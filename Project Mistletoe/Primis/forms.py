from django import forms
from apps.models import StudentForm 
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = StudentForm  
        fields = "__all__"
