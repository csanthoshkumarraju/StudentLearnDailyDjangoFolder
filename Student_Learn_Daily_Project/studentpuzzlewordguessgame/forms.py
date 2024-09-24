from django import forms

class PuzzleGuessForm(forms.Form):
    guess_word = forms.CharField(
        label='Word',
        widget=forms.TextInput(attrs={
            'id': 'puzzle-word-game',
            'placeholder': 'Enter your guess',
            'class': 'puzzle-word-guess-input',
            'required': 'required'
        })
    )

