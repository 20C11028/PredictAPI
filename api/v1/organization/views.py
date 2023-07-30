from rest_framework.generics import (ListCreateAPIView)
from rest_framework.permissions import AllowAny

from InputObject.models import InputObject
from . import serializer


class OrganizationAPI(ListCreateAPIView):
    queryset = InputObject.objects.all()
    serializer_class = serializer.InputObjectSerializer
    permission_classes = (AllowAny,)