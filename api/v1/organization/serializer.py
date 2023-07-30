from rest_framework import serializers
from InputObject.models import InputObject


class InputObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = InputObject
        fields = "__all__"