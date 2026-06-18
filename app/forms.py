from django import forms
from .models import contactform
from django.core.validators import RegexValidator
class Contact_Form(forms.ModelForm):
    indian_phone_regex=RegexValidator(regex=r'^(\+91|0)?[6-9]\d{9}$',message="Please enter a valid number")
    phone_number=forms.CharField(validators=[indian_phone_regex],max_length=15,
    widget=forms.TextInput(attrs={'class': 'form-control bg-theme-dark p-3 border-0','placeholder': '9876543210'}))
    name_validator = RegexValidator(
        regex=r'^[A-Za-z ]+$',
        message="Name should contain only letters and spaces."
    )
    name = forms.CharField(
        validators=[name_validator],
        widget=forms.TextInput(attrs={
            'class': 'form-control bg-theme-dark p-3 border-0',
            'placeholder': 'Your Full Name'
        })
    )
    class Meta:
        model=contactform
        fields=['name','email','phone_number','message']
#css
        widgets={
            
            'email':forms.EmailInput(attrs={'class':'form-control bg-theme-dark p-3 border-0','placeholder':'name@example.com'}),
            'message':forms.Textarea(attrs={'class':'form-control bg-theme-dark p-3 border-0','rows':4,'placeholder':'Your Message'})
}