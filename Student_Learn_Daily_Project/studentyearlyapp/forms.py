from django import forms 
from .models import studentyearlyplan

class studentyealyform(forms.ModelForm):
    class Meta:
         model = studentyearlyplan
         fields = ['yearly_plan',]
         widgets = {
              'yearly_plan':forms.TextInput(attrs={
                   'placeholder': 'Enter your yearly Plan here', 
                   'class': 'Add-yearly-plan-input-box'
              })
         }