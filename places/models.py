from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Локация')
    description_short = models.TextField()
    description_long = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, verbose_name='Долгота')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
