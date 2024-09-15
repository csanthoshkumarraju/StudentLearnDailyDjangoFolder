from django import forms
from .models import StudentHomeworkModel

class StudentHomeworkForm(forms.ModelForm):
    class Meta:
        model = StudentHomeworkModel
        fields = ['subject_name', 'topic_name']
        widgets = {
            'subject_name': forms.TextInput(attrs={'placeholder': 'Subject Name', 'class': 'text-input'}),
            'topic_name': forms.TextInput(attrs={'placeholder': 'Topic Name', 'class': 'text-input'}),
        }

      