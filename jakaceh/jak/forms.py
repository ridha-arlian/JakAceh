from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Profile


class EditUserProfileForm(UserChangeForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'username', 'placeholder': "Enter your Username"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'user-desc', 'placeholder': "Enter your email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'user-title', 'placeholder': "Enter your first name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'user-desc', 'placeholder': "Enter your last name"}))
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "type":"text",
            "name":"username",
            "class":"form-control isi",
        }),
        self.fields["email"].widget.attrs.update({
            "type":"text",
            "name":"email",
            "class":"form-control isi",
        }),
        self.fields["first_name"].widget.attrs.update({
            "type":"text",
            "name":"first_name",
            "class":"form-control isi",
        }),
        self.fields["last_name"].widget.attrs.update({
            "type":"text",
            "name":"last_name",
            "class":"form-control isi",
        }),
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
