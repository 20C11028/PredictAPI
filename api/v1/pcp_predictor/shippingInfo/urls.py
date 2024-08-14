from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('classify/', views.call_model.as_view()),
]
