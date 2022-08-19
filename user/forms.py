from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Введите адрес эл. почты'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль'}))


    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password1', 'password2')


    def __init__(self, *agrs, **kwargs):
        super(RegisterForm, self).__init__(*agrs, **kwargs)
        for field_name, field in self.fields.items():
            # значенеи в словаре attrs с ключём class применяется ко всем wigts в классе UserRegistrationForm
            field.widget.attrs['class'] = 'form-control py-4'


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *agrs, **kwargs):
        super(LoginForm, self).__init__(*agrs, **kwargs)
        for field_name, field in self.fields.items():
            # значенеи в словаре attrs с ключём class применяется ко всем wigts в классе UserLoginForm
            field.widget.attrs['class'] = 'form-control py-4'