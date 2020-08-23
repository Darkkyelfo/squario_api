from django.db import models
from squario.aquarios.models import Aquarium


# Create your models here.


class NumericSensor(models.Model):
    """
        Classe que representa os sensores que guardam valores numericos.
    """
    value = models.FloatField()
    name = models.CharField(max_length=90)
    type = models.CharField(max_length=50)
    aquarium = models.ForeignKey(Aquarium, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "numeric_sensors"

    @staticmethod
    def get_serialized_fields():
        return ["id", "value", "type", "created_at"]
