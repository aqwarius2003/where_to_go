from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Place


def index(request):
    places = Place.objects.all()

    feature_collection = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.longitude, place.latitude]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse('place', kwargs={'place_id': place.id})
    }
            }
            for place in places
        ]
    }

    return render(request, 'index.html', context={
        'places': feature_collection
    })


def place_detail(request, place_id):
    place = get_object_or_404(Place.objects.prefetch_related('photos'), id=place_id)

    place_details = {
        'title': place.title,
        'imgs': [image.img.url for image in place.photos.all()],
        'short_description': place.short_description,
        'long_description': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        }
    }

    return JsonResponse(
        place_details,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )