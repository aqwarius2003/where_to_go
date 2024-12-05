from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.http import JsonResponse


def index(request):
    places = Place.objects.all()

    places_data = {
        "type": "FeatureCollection",
        "features": []
    }

    for place in places:
        places_data["features"].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.longitude, place.latitude]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.id,  # id of the place
                    "detailsUrl": reverse('place', kwargs={'place_id': place.id})
                }
            },
        )

    return render(request, 'index.html', context={
        'places': places_data
    })


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    place_details = {
        "title": place.title,
        "imgs": [image.img.url for image in place.photos.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.latitude,
            "lng": place.longitude,
        }
    }

    return JsonResponse(
        place_details,
        json_dumps_params={'ensure_ascii': False, 'indent': 4}
    )