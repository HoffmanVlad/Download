from dataclasses import field
from pyexpat import model
from django import forms
from .models import CustomUser, Watch, Phone

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'repeat_password')

    def clean(self):
        data = self.cleaned_data
        if data.get('password') != data.get('repeat_password'):
            raise forms.ValidationError('Passwords do not match!')
        return data

class WatchForm(forms.ModelForm):
    class Meta:
        model = Watch
        fields = '__all__'

class PhoneForm(forms.ModelForm):
    class Meta:
        model = Phone
        fields = '__all__'