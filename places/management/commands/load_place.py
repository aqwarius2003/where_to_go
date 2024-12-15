import os
import re
from urllib.parse import urljoin, urlparse

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from requests import RequestException

from places.models import Photo, Place


class Command(BaseCommand):
    help = 'Загружает данные из JSON-файлов в базу данных и скачивает фотографии'

    def add_arguments(self, parser):
        parser.add_argument('urls', nargs='+', type=str, help='Ссылки на JSON файлы или папкe с данными c github')

    def handle(self, *args, **options):
        urls = options['urls']
        for url in urls:
            if url.endswith('.json'):
                self.process_json(self.convert_to_raw(url))
            else:
                self.process_folder(url)

    @staticmethod
    def convert_to_raw(link):
        if "github.com" in link:
            link = link.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
        return link

    def process_folder(self, folder_url):
        response = requests.get(folder_url)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR(f'Не удалось получить данные с {folder_url}'))
            return

        html_content = response.text
        raw_json_links = re.findall(r'href="(/devmanorg/where-to-go-places/blob/master/places/.*?\.json)"',
                                    html_content)
        base_url = "https://raw.githubusercontent.com"
        json_links = [urljoin(base_url, link.replace('/blob/', '/')) for link in raw_json_links]

        for json_url in json_links:
            self.stdout.write(self.style.NOTICE(f'\nОбрабатыввется ссылка:\n{json_url}'))
            self.process_json(json_url)

    def process_json(self, json_url):
        try:
            response = requests.get(json_url)
            response.raise_for_status()
        except RequestException as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при получении данных с {json_url}: {e}'))
            return

        try:
            data = response.json()
        except ValueError as e:
            self.stdout.write(self.style.ERROR(f'Ошибка при разборе JSON с {json_url}: {e}'))
            return

        # Проверка на существование локации
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

        # Независимо от того, была ли локация создана, проверяем и загружаем фотографии
        for order, img_url in enumerate(data['imgs']):
            img_name = os.path.basename(urlparse(img_url).path)

            # Проверка на существование фотографии
            if not Photo.objects.filter(place=place, img__endswith=img_name).exists():
                try:
                    img_response = requests.get(img_url)
                    img_response.raise_for_status()
                    photo = Photo(
                        place=place,
                        order=order
                    )
                    photo.img.save(img_name, ContentFile(img_response.content), save=True)
                    self.stdout.write(self.style.SUCCESS(f'Фото "{img_name}" добавлено.'))
                except RequestException as e:
                    self.stdout.write(self.style.ERROR(f'Не удалось загрузить фото с {img_url}: {e}'))
            else:
                self.stdout.write(self.style.WARNING(f'Фото "{img_name}" уже существует для локации "{place.title}".'))

        self.stdout.write(self.style.SUCCESS(f'Данные локации "{place.title}" успешно загружены.'))