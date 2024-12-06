from django.core.management.base import BaseCommand, CommandError
import requests
from places.models import Place, Photo
from django.core.files.base import ContentFile
from urllib.parse import urlparse
import os


class Command(BaseCommand):
    help = 'Загружает данные из JSON-файла в базу данных и скачивает фотографии'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='Ссылка на JSON файл или папку с данными')

    def handle(self, *args, **options):
        json_url = options['json_url']
        response = requests.get(json_url)
        if response.status_code != 200:
            raise CommandError(f'Не удалось получить данные с {json_url}')

        data = response.json()

        place, created = Place.objects.get_or_create(
            title=data['title'],
            defaults={
                'description_short': data.get('description_short', ''),
                'description_long': data.get('description_long', ''),
                'latitude': data['coordinates']['lat'],
                'longitude': data['coordinates']['lng'],
            }
        )

        if not created:
            self.stdout.write(self.style.WARNING(f'Локация "{place.title}" уже существует.'))

        for order, img_url in enumerate(data['imgs']):
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_name = os.path.basename(urlparse(img_url).path)
                photo = Photo(
                    place=place,
                    order=order
                )
                photo.img.save(img_name, ContentFile(img_response.content), save=True)
                self.stdout.write(self.style.SUCCESS(f'Фото "{img_name}" добавлено.'))
            else:
                self.stdout.write(self.style.ERROR(f'Не удалось загрузить фото с {img_url}'))

        self.stdout.write(self.style.SUCCESS(f'Данные для места "{place.title}" успешно загружены.'))