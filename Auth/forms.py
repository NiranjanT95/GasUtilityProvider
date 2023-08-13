from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Username/Email", required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=True)