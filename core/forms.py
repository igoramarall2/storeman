from django import forms
from .models import Category, Product, Client, Order
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


FORM_INPUT_CLASS = "form-control"


class LoginForm(AuthenticationForm):
    
    class Metal:
        model = User
        fields = ("username","password")



    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": FORM_INPUT_CLASS, "placeholder": "Usuário"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": FORM_INPUT_CLASS, "placeholder": "Senha"}
        )
    )


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name",)

        widgets = {"name": forms.TextInput(attrs={"class": FORM_INPUT_CLASS})}


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

        widgets = {
            "codprod": forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}),
            "nameprod": forms.TextInput(attrs={"class": FORM_INPUT_CLASS}),
            "priceprod": forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}),
            "desprod": forms.Textarea(attrs={"class": FORM_INPUT_CLASS}),
            "avprod": forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}),
            "catprod": forms.Select(attrs={"class": FORM_INPUT_CLASS}),
        }


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": FORM_INPUT_CLASS}),
            "email": forms.EmailInput(attrs={"class": FORM_INPUT_CLASS}),
            "cpf": forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}),
            "phone": forms.NumberInput(attrs={"class": FORM_INPUT_CLASS}),
        }


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "client",
            "products",
        )

        widgets = {
            "client": forms.Select(attrs={"class": FORM_INPUT_CLASS}),
            # 'products': forms.Select(attrs={'class': FORM_INPUT_CLASS}),
        }
