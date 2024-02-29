"""
URL configuration for storeman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from core import views
from core.forms import LoginForm
from core.functions import save_orders
from core.views import (
    category,
    clients,
    consulta_pedidos,
    index,
    login_view,
    logoutwebsite,
    orders,
    products,
)

app_name = "core"


urlpatterns = [
    path("", index, name="index"),
    path("admin/", admin.site.urls),
    path("nova_categoria/", views.novacategoria, name="nova_categoria"),
    path("novos_items/", views.products, name="novos_items"),
    path("category/", category, name="category"),
    path("products/", products, name="products"),
    path("clientes/", clients, name="clients"),
    path("orders/", orders, name="orders"),
    path("saveorders/", save_orders, name="saveorders"),
    path("consultar_pedidos/", consulta_pedidos, name="consultar_pedidos"),
    path("login/", login_view, name="login"),
    path("logout/", logoutwebsite, name="logout"),
    path("produtos_cadastrados/", views.produtos_cadastrados, name="produtos_cadastrados"),

]
