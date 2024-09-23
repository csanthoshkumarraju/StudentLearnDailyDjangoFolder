from django import forms

class WordGuessForm(forms.Form):
    word_game = forms.CharField(label='Word', max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your guess',
        'class': 'word-guess-input'
    }))
