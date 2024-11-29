from django.shortcuts import render
from .models import Place
from django.shortcuts import get_object_or_404


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
                    "placeId": place.title,  # id of the place
                    "detailsUrl": "static/places/roofs24.json"
                }
            },
        )

    return render(request, 'index.html', context={
        'places': places_data
    })


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    place_detail= {
        "type": "Feature",
        "geometry": {
            "type": "Point",
            "coordinates": [place.latitude]
        },
        "properties": {
            "title": place.title,
            "description_short": place.description_short,
            "description_long": place.description_long,
            "placeId": place.title,
            "detailsUrl": "static/places/roofs24.json"
        }
    }
    return render(request, 'place_detail.html', context={
        'place': place_detail
    })