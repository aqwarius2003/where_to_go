from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Локация')
    description_short = models.TextField()
    description_long = models.TextField()
    latitude = models.FloatField(verbose_name='Широта', null=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'


class Photo(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='photos')
    img = models.ImageField(upload_to='places', verbose_name='Фото')
    order = models.IntegerField(default=0, verbose_name='Порядковый номер')

    def __str__(self):
        return f'{self.order} {self.place.title}'
