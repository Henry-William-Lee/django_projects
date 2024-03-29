"""Django_Checkbook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.urls import path
from . import views
from django.shortcuts import render,redirect,get_object_or_404
from .models import Account, Transaction
from .forms import AccountForm, TransactionForm

urlpatterns = [
    path('', views.home,name='index'),
    path('create/',views.create_account,name='create'),
    path('balance/', views.balance, name='balance'),
    path('transaction/', views.transaction, name='transaction'),
    path('<int:pk>/balance/', views.balance, name ='balance'),


]
