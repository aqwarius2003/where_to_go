from django.contrib import admin
from .models import Place, Photo


# @admin.register(Place)
# class PlaceAdmin(admin.ModelAdmin):
#     list_display = ('title')
#     search_fields = ('title')
#
# admin.site.register(Place, PlaceAdmin)

admin.site.register(Place)

admin.site.register(Photo)
