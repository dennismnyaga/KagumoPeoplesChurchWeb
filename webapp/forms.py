from django import forms
from .models import Giving
from django.forms import ModelForm
# class NameForm(forms.Form):
#     first_name = forms.CharField(label='First name', max_length=100)

class GiveForm(ModelForm):
    class Meta:
        model = Giving
        fields = '__all__'