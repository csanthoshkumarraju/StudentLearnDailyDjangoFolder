from django import forms 
from .models import studentmonthlyplanmodel

class studentmonthlyform(forms.ModelForm):
      class Meta:
            model = studentmonthlyplanmodel
            fields = ['student_monthly_plan',]
            widgets = {'student_monthly_plan':forms.TextInput(attrs={'placeholder': 'Enter your monthly Plan here', 'class': 'Add-monthly-plan-input-box'})}
