"""jangogpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app import views
from django.urls import path


urlpatterns = [
    path('',views.sayhello),#demo test interface
    path('callback', views.callback),#reply user enter message
    path('line_bot_webhook', views.line_bot_webhook),#ollama chat use regular model
    path('OpenWebUI_webhook', views.OpenWebUI_webhook),# OpenWebUI chat you can use RAG model chat here
]


