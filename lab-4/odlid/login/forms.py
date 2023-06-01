from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.formfields import PhoneNumberField
from .models import Client


class RegistrationForm(UserCreationForm):
    username = forms.CharField(min_length=4, max_length=20)
    email = forms.EmailField(required=True)
    unique_code = forms.IntegerField(required=True)
    phone = PhoneNumberField(region="BY")
    city = forms.CharField(
        max_length=50,
    )
    address = forms.CharField(max_length=50)
    password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)

    field_order = [
        "username",
        "email",
        "unique_code",
        "phone",
        "city",
        "address",
        "password1",
        "password2",
    ]

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
        labels = {"user_name": "*Username", "password": "*Password"}
        widgets = {
            "user_name": forms.TextInput(
                attrs={"placeholder": "ex:test", "autocomplete": "off"}
            ),
            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "********",
                    "autocomplete": "off",
                    "data-toggle": "password",
                }
            ),
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


# class RegistrationAdminForm(UserCreationForm):
#     username = forms.CharField(min_length=4, max_length=20)
#     email = forms.EmailField(required=True)
#     unique_code = forms.IntegerField(required=True)
#     phone = PhoneNumberField(region="BY")
#     city = forms.CharField(
#         max_length=50,
#     )
#     address = forms.CharField(max_length=50)
#     password1 = forms.CharField(label = 'Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label = 'Confirm Password',widget=forms.PasswordInput)

#     field_order = [
#         "username",
#         "email",
#         "unique_code",
#         "phone",
#         "city",
#         "address",
#         "password1",
#         "password2",
#     ]

#     class Meta:
#         model = Employee
#         fields = {
#             "username",
#             "email",
#             "unique_code",
#             "phone",
#             "city",
#             "address",
#             "password1",
#             "password2",
#         }
#         labels = {"user_name": "*Username", "password": "*Password"}
#         widgets = {
#             "user_name": forms.TextInput(
#                 attrs={"placeholder": "ex:test", "autocomplete": "off"}
#             ),
#             "password": forms.PasswordInput(
#                 attrs={
#                     "placeholder": "********",
#                     "autocomplete": "off",
#                     "data-toggle": "password",
#                 }
#             ),
#         }

#     def save(self, commit: bool = ...):
#         user = super(RegistrationForm, self).save(commit=False)

#         user.email = self.cleaned_data["email"]
#         user.unique_code = self.cleaned_data["unique_code"]
#         user.phone = self.cleaned_data["phone"]
#         user.is_staff = True;
#         user.city = self.cleaned_data["city"]
#         user.address = self.cleaned_data["address"]

#         if commit:
#             user.save()

#         return user
