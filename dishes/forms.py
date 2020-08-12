from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from . models import *


class LoginUserForm(AuthenticationForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'main-form-input'


class AuthUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'main-form-input'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class SearchForm(forms.Form):
    keyword = forms.CharField(max_length=50, label='Искомое слово')
    #dishes = forms.ModelChoiceField(queryset=Dishes.objects.all(), label='Блюда')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'col-md-3'


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = {'name', 'tag', 'deception'}


