from django.db import models
from embed_video.fields import EmbedVideoField
# Create your models here.

class CityName(models.Model):
    city_name = models.CharField(max_length=200)
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.city_name

class AreaName(models.Model):
    city_name = models.ForeignKey(CityName, default = 1, verbose_name = 'Area', on_delete=models.SET_DEFAULT)
    area_name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    objects = models.Manager()
    class Meta:
        verbose_name_plural = 'Areas'

    def __str__(self):
        return self.area_name
