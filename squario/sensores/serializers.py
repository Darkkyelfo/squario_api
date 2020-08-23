from squario.sensores.models import NumericSensor

from rest_framework import serializers


class NumericSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumericSensor
        fields = NumericSensor.get_serialized_fields()



