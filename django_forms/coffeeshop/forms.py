from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from . import models


class NameForm(forms.Form):
    name = forms.CharField(label="Your name", min_length=3, max_length=100)  # <input type="text">

    def save(self):
        pass


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password', 'email')
        # fields = '__all__' # nie robić tak
        # exclude = ('email',)

    def save(self, commit=True):
        m = super().save(commit=False)
        m.password = make_password(self.cleaned_data.get('password'))
        m.username = self.cleaned_data.get('username').lower()

        if commit:
            m.save()
        return m


