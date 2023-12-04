from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('organization/', include('api.v1.organization.urls')),
    path('predictor/', include('api.v1.predictor.urls')),
    path('pcp_predictor/', include('api.v1.pcp_predictor.urls')),
]
