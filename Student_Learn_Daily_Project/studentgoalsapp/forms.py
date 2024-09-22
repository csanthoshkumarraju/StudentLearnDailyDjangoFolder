from django import forms
from .models import studentgoalsmodel

class studentgoalform(forms.ModelForm):
    class Meta:
        model = studentgoalsmodel
        fields = ['goal',]
        widgets = {
            'goal':forms.TextInput(attrs={
                'placeholder': 'Enter your goals here',
                'class': 'add-goal-input-box'
            })

        }