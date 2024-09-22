from django import forms 
from .models import studentnotesmodel

class studentnotesform(forms.ModelForm):
    class Meta:
        model = studentnotesmodel
        fields = ['notes']
        widgets = {
            'notes':forms.TextInput(attrs={
                'placeholder':'Add your notes',
                'class':'add-notes-input-box'
            })
        }