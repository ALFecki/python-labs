from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Client


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    unique_code = forms.IntegerField(
        required=True, help_text="Enter your company unique code"
    )
    phone = PhoneNumberField(region="BY")
    city = forms.CharField(max_length=50, help_text="Enter the city of your company")
    address = forms.CharField(max_length=50, help_text="Enter your company address")

    class Meta:
        model = Client
        fields = {
            "username",
            "email",
            "unique_code",
            "phone",
            "city",
            "address",
            "password1",
            "password2",
        }

    def save(self, commit: bool = ...):
        user = super(RegistrationForm, self).save(commit=False)

        user.email = self.cleaned_data["email"]
        user.unique_code = self.cleaned_data["unique_code"]
        user.phone = self.cleaned_data["phone"]
        user.city = self.cleaned_data["city"]
        user.address = self.cleaned_data["address"]

        if commit:
            user.save()

        return user
