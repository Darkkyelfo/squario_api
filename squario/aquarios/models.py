from django.db import models


# Create your models here.

class Aquarium(models.Model):
    """ Classe que representa os aquarios um usuario """
    name = models.TextField
    width = models.FloatField(null=True)
    height = models.FloatField(null=True)
    length = models.FloatField(null=True)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "aquarium"

    @staticmethod
    def get_serialized_fields():
        return ["id", "name", "width", "length", "active", "deleted", 'actions', "created_at"]


class AquariumAction(models.Model):
    """ Classe que representa as acoes que um aquario pode realizar """
    action = models.CharField(max_length=50)
    aquarium = models.ForeignKey(Aquarium, related_name='actions', on_delete=models.CASCADE)
    input_pin = models.IntegerField
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "aquarium_action"

    @staticmethod
    def get_serialized_fields():
        return ["id", "action", "input_pin", "created_at"]
