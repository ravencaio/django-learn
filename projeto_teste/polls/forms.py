from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=200, label = 'Título')
    text = forms.CharField(widget = forms.Textarea, label = 'Texto')
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label = 'Usuário')
    password = forms.CharField(widget = forms.PasswordInput, label = 'Senha')

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=150, label = 'Usuário')
    password = forms.CharField(widget = forms.PasswordInput, label = 'Senha')
    email = forms.EmailField(label = 'Email')