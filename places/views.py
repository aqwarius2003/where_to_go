from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse


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
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude,
        }
    }

    return JsonResponse(
        place_details,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )
