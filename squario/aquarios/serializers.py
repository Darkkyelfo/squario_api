from squario.aquarios.models import Aquarium, AquariumAction

from rest_framework import serializers


class AquariumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aquarium
        fields = Aquarium.get_serialized_fields()


class AquariumActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AquariumAction
        fields = AquariumAction.get_serialized_fields()
