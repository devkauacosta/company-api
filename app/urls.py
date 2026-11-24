
from django.contrib import admin
from django.urls import path
from sector.views import sector_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sectors/', sector_view, name='sectors')
]
