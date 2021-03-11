from django import forms        # проверить
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm

from .models import InfojobUser


class InfojobUserLoginForm(AuthenticationForm):
    class Meta:
        model = InfojobUser
        fields = ('email', 'password', 'user_role')

    def __init__(self, *args, **kwargs):
        super(InfojobUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class InfojobUserRegisterForm(UserCreationForm):
    class Meta:
        model = InfojobUser
        fields = ('email', 'password1',  'password2', 'user_role')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class InfojobUserEditForm(UserChangeForm):
    class Meta:
        model = InfojobUser
        fields = ('email', 'user_role', 'avatar', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'pasword':
                field.widget = forms.HiddenInput()
