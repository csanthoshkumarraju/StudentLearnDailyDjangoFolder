from django import forms
from .models import studentassignmentsmodel

class studentassignmentsform(forms.ModelForm):
    class Meta:
        model = studentassignmentsmodel
        fields = ['assignment',]
        widgets = {
            'assignment': forms.TextInput(attrs={'placeholder': 'Add an assignment by including the subject name, topic, due date, and assignment description.', 'class': 'Add-assignment-input-box'})
            }


    
