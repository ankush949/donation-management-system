from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Donation, Contact


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")

        if password and confirm and password != confirm:
            raise ValidationError("Passwords do not match.")
        return cleaned_data
    

class LoginForm(forms.Form):
    username=forms.CharField()    
    password= forms.CharField(widget=forms.PasswordInput)


class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['category', 'item_description', 'quantity']
        widgets = {
            'category': forms.Select(attrs={'class':'form-select'}),
            'item_description':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'quantity':forms.NumberInput(attrs={'class':'form-control'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields=['name','email','phone_number','subject','message','consent']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Your Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email'}),
            'phone_number':forms.NumberInput(attrs={'class':'form-control','placeholder':'Your Phone Number'}),
            'subject':forms.Textarea(attrs={'class':'form-control','rows':2, 'placeholder':'Subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','rows':5,'placeholder':'Your Message'}),
            'consent':forms.CheckboxInput(attrs={'class':'form-check-input'})

        }
