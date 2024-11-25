from django.db import models

# Create your models here.
class Place(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name='Локация')
    description_short = models.TextField()
    description_long = models.TextField()
    latitude = models.DecimalField(max_digits=10, decimal_places=8, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=11, decimal_places=8, verbose_name='Долгота')
    coordinates = models.PointField(srid=4326)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Переопредеение метода save для автоматической установки координат."""
        self.coordinates = Point(float(self.longitude), float(self.latitude))
        super().save(*args, **kwargs)

    def get_latitude(self):
        """Возвращает широту."""
        return self.latitude

    def get_longitude(self):
        """Возвращает долготу."""
        return self.longitude

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

