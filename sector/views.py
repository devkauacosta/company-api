from django.shortcuts import render
from django.http import JsonResponse
from .models import Sector

def sector_view(request):
    if request.method == "GET":
        sectors = Sector.objects.all()
        data = [
            {"id": sector.id, "name": sector.name}
            for sector in sectors
        ]

        return JsonResponse(data, safe=False)