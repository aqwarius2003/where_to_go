from django.contrib import admin
from .models import Place, Photo
from django.utils.html import format_html

def generate_image_preview(obj):
    if hasattr(obj, 'img') and obj.img:
        return format_html('<img src="{}" style="height: 100px;" />', obj.img.url)
    return "No Image"

class PlaceImageInline(admin.TabularInline):
    model = Photo
    extra = 0
    verbose_name = 'Фото'
    verbose_name_plural = 'Фотографии'
    fields = ('img', 'order', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        return generate_image_preview(obj)

    image_preview.short_description = 'Превью'


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [PlaceImageInline]


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    fields = ('place', 'order', 'img', 'image_preview')
    readonly_fields = ('image_preview',)
    list_display = ('place', 'order', 'image_preview')
    list_editable = ('order',)
    ordering = ('place', 'order')

    def image_preview(self, obj):
        return generate_image_preview(obj)

    image_preview.short_description = 'Превью'


