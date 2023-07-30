from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('organization/', include('api.v1.organization.urls')),
    path('predictor/', include('api.v1.predictor.urls')),
]
