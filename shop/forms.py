from django import forms
from django.core.validators import RegexValidator

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search For Products'}), label=False)

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField()
    phone_numbre = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

