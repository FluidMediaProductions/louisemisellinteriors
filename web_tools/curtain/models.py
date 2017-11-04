from django.db import models


class Fabric(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField('Repeatable Image')
    width = models.IntegerField('Width (cm)')
    repeat = models.IntegerField('Pattern repeat (cm)')
    price = models.FloatField('Price per meter')

    def __str__(self):
        return self.name
