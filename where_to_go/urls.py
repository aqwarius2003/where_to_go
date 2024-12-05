from django.contrib import admin
from django.urls import path
from places import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='index'),
                  path('place/<int:place_id>/', views.place_detail, name='place'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
