from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from catalog.models import Product, Employee


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class EmployeeCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Employee
        fields = UserCreationForm.Meta.fields + (
            "employee_number",
            "first_name",
            "last_name",
        )

    def clean_employee_number(self):
        return validate_employee_number(self.cleaned_data["employee_number"])


class EmployeeNumberUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ["employee_number"]

    def clean_brand(self):
        return validate_employee_number(self.cleaned_data["employee_number"])


def validate_employee_number(employee_number):
    if len(employee_number) != 8:
        raise ValidationError("Employee number must be exactly 8 characters")
    if not employee_number[:3].isupper() or not employee_number[:3].isalpha():
        raise ValidationError("First 3 characters must be uppercase letters")
    if not employee_number[3:].isdigit():
        raise ValidationError("Last 5 characters must be digits")
    return employee_number



class ProductSearchForm(forms.Form):
    model = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )


class EmployeeSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )


class BrandSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by name"}),
    )
