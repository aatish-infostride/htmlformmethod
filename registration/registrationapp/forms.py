from django import forms


class signupform(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class loginform(forms.Form):
    name = forms.EmailField(max_length=100,)
    password = forms.CharField(widget=forms.PasswordInput)
