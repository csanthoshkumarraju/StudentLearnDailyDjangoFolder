from django import forms
from .models import studentcollabaratemodel

class studentvollabarateforms(forms.ModelForm):
    class Meta:
        model = studentcollabaratemodel
        fields = ['message',]
        widgets = {'message':forms.TextInput(attrs={
            'placeholder':'Send a message',
            'class':'send-messege-input-box'
        })}