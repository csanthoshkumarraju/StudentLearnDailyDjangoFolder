from django import forms
from .models import studentdailymodel

class studentdailyplan(forms.ModelForm):
    class Meta:
        model = studentdailymodel
        fields = ['daily_plan',]
        widgets = {'daily_plan':forms.TextInput(attrs={'placeholder': 'Enter your daily Plan here', 'class': 'Add-daily-plan-input-box'})}

    
