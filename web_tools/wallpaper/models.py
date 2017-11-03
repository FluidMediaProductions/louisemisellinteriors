from django.db import models


class Wallpaper(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField('Repeatable Image')
    width = models.IntegerField('Width (cm)')
    roll_length = models.FloatField('Roll length (m)')
    repeat = models.IntegerField('Pattern repeat (cm)')
