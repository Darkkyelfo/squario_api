from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from squario.sensores.models import NumericSensor
from squario.sensores.serializers import NumericSensorSerializer


@api_view(["GET", "POST"])
def sensor_by_aquarium(request):
    if request.method == "GET":
        numeric_sensor = NumericSensor.objects.all()
        serializer = NumericSensorSerializer(numeric_sensor, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = NumericSensorSerializer(data=request.data)
        if serializer.is_valid():
            # aquarium_id = serializer.data.get("aquarium")
            # serializer.save(aquarium=Aquarium.objects.get(pk=aquarium_id))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
