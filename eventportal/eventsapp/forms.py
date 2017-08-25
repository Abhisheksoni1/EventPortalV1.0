from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    SEX_CHOICES = (('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER'))
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    name = forms.CharField(max_length=128)
    sex = forms.CharField(max_length=10)