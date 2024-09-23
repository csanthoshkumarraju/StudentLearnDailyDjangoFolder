from django import forms

class NumberGuessForm(forms.Form):
    number_game = forms.IntegerField(
        label="Number",
        min_value=1,
        max_value=10,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Enter your guess',
            'class': 'number-guess-input',
        }),
        required=True
    )
