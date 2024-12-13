from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Локация')
    short_description = models.TextField(verbose_name='Краткое описание', blank=True)
    long_description = HTMLField(verbose_name='Детальное описание', blank=True)
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['title']

    def __str__(self):
        return self.title


class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='photos', verbose_name='Локация')
    img = models.ImageField(verbose_name='Фото')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер', db_index=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.order}'
