import json
from datetime import datetime

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import logout
from .forms import CategoryForm, ClientsForm, LoginForm, OrdersForm, ProductForm
from .models import Category, Client, Order, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import redirect, render

# Create your views here.


def index(request):
    return render(request, "core/index.html")


def login_view(request):
    if request.method == "POST":
        print("entrou no post")
        print("form valido")
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")  # Redirect to home page after successful login
        else:
            return HttpResponse("Invalid username or password.")
    else:
        form = LoginForm()
        print("nao deu certo")

    return render(
        request,
        "core/login.html",
        {"title": "Login", "button_text": "Log in", "form": form},
    )


@login_required
def logoutwebsite(request):
    logout(request)
    return HttpResponseRedirect("/")


def novacategoria(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CategoryForm()
    category = Category.objects.all()
    return render(
        request,
        "core/categoria.html",
        {
            "title": "Nova Categoria",
            "form": form,
            "category": category,
            "button_text": "Cadastrar nova Categoria",
        },
    )


def category(request):
    return render(request, "core/category.html")


def products(request):
    if request.method == "POST":
        print("entrou")
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            form = ProductForm()
        else:
            print(form.errors)
    else:
        form = ProductForm()

    return render(
        request,
        "core/products.html",
        {"title": "Novos Items", "form": form, "button_text": "Cadastrar Produto"},
    )


def clients(request):
    if request.method == "POST":
        form = ClientsForm(request.POST)
        if form.is_valid():
            form.save()
            form = ClientsForm()
        else:
            print(form.errors)
    else:
        form = ClientsForm()

    return render(
        request,
        "core/clients.html",
        {"title": "Clientes", "form": form, "button_text": "Cadastrar Cliente"},
    )


def orders(request):
    total_products = Product.objects.all()
    clients = [(client.id, client.name) for client in Client.objects.all()]

    return render(
        request,
        "core/orders.html",
        {"title": "Pedidos", "products": total_products, "clients": clients},
    )


def consulta_pedidos(request):
    # Prefetch related products to avoid N+1 query issue
    orders = Order.objects.prefetch_related("products")

    return render(
        request,
        "core/list_orders.html",
        {
            "title": "Consultar Pedidos",
            "orders": orders,
        },
    )

def produtos_cadastrados(request):
    products = Product.objects.all()
    print(products)
    return render(
        request,
        "core/produtos_cadastrados.html",
        {
            "title": "Produtos Cadastrados",
            "produtos": products,
        },
    )