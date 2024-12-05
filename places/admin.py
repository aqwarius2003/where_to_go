from django.contrib import admin
from .models import Place, Photo


class PlaceImageInline(admin.TabularInline):
    model = Photo

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('place', 'order')
    list_editable = ('order',)
    ordering = ('place', 'order')

    def place(self, obj):
        return obj.place.title
