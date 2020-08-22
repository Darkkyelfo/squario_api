from django.db import models


# Create your models here.

class Aquarium(models.Model):
    """ Classe que representa as aquarios um usuario """
    name = models.TextField
    width = models.FloatField(null=True)
    height = models.FloatField(null=True)
    length = models.FloatField(null=True)
    active = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "aquarium"

class AquariumAction(models.Model):
    action = models.CharField(max_length=50)
    aquarium = models.ForeignKey(Aquarium,on_delete=models.CASCADE)
    input_pin = models.IntegerField
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "aquarium_action"


