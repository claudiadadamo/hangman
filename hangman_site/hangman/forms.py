from django import forms

class GuessForm(forms.Form):
    guess = forms.CharField(label='Your guess', max_length=100, widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))


