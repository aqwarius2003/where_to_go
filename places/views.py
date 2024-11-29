from django.shortcuts import render
from .models import Place


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
