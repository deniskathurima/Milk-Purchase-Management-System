from django import forms
from .models import Register, MilkRecord


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['firstName', 'lastName', 'email', 'mobileNumber']


class MilkRecordForm(forms.ModelForm):
    class Meta:
        model = MilkRecord
        fields = ['farmer', 'milk_qty']

