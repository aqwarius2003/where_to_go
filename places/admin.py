from django.contrib import admin
from .models import Place, Photo
from django.utils.html import format_html
from adminsortable2.admin import SortableStackedInline
from adminsortable2.admin import SortableAdminBase


def generate_image_preview(obj):
    if hasattr(obj, 'img') and obj.img:
        return format_html('<img src="{}" style="height: 100px;" />', obj.img.url)
    return "No Image"


class PlaceImageStackedInline(SortableStackedInline):
    model = Photo
    extra = 0
    verbose_name = 'Фото'
    search_fields = ['place__title']
    verbose_name_plural = 'Фотографии'
    fields = ['img', 'order', 'image_preview']
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return generate_image_preview(obj)

    image_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [PlaceImageStackedInline]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ('place', 'order', 'img', 'image_preview')
    readonly_fields = ('image_preview',)
    list_display = ('place', 'order', 'image_preview')
    ordering = ('place', 'order')

    def image_preview(self, obj):
        return generate_image_preview(obj)

    image_preview.short_description = 'Превью'
