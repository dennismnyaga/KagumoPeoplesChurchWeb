from django import forms
from .models import Giving
from django.forms import ModelForm, TextInput, EmailInput
from django.forms import ModelForm
from .models import *
# class NameForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=100)


class SubscriberForm(ModelForm):
    class Meta:
        model = Subcribers
        fields = ['email']

        widgets = {
            'email': EmailInput(attrs={
                'class': "form-control", 
                'style': 'background: none;border: 1px solid #fff;border-radius: 30px;color: #fff;display: inline-block;font-size: 15px;font-weight: 300;height: 57px;margin-right: 17px;padding-left: 35px;width: 70%;cursor: pointer;',
                'placeholder': 'Email'
                })
        }

        # widget=forms.EmailInput(attrs={'class': 'form-control'})

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email

class MailMessageForm(forms.ModelForm):
    class Meta:
        model = MailMessage
        fields = '__all__'