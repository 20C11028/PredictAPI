from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('chem/', include('api.v1.pcp_predictor.chem.urls')),
    path('chemRegulatory/', include('api.v1.pcp_predictor.chemRegulatory.urls')),
    path('hazardousWaste/', include('api.v1.pcp_predictor.hazardousWaste.urls')),
    path('chemColorOdor/', include('api.v1.pcp_predictor.chemColorOdor.urls')),
    path('phyChemRegulatory/', include('api.v1.pcp_predictor.phyChemRegulatory.urls')),
    path('phyState/', include('api.v1.pcp_predictor.phyState.urls')),
    path('otherProps/', include('api.v1.pcp_predictor.otherProps.urls')),
    path('regulatoryClassification/', include('api.v1.pcp_predictor.regulatoryClassification.urls')),
    path('regulatoryEPA/', include('api.v1.pcp_predictor.regulatoryEPA.urls')),
    path('shippingInfo/', include('api.v1.pcp_predictor.shippingInfo.urls')),
    path('landBan/', include('api.v1.pcp_predictor.landBan.urls')),
    path('UNNumber/', include('api.v1.pcp_predictor.UNNumber.urls')),
]
