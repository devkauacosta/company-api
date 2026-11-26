import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Sector
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def sector_create_list_view(request):
    if request.method == "GET":
        sectors = Sector.objects.all()
        data = [
            {"id": sector.id, "name": sector.name}
            for sector in sectors
        ]

        return JsonResponse(data, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        new_sector = Sector(name=data['name']).save()
        return JsonResponse(
            {'id': new_sector.id, 'name': new_sector.name},
            status=201
        )


def sector_detail_view(request, pk):
    sector = get_object_or_404(Sector, pk=pk)
    data = {
        "id": sector.id, 
        "name": sector.name
    }
    return JsonResponse(data)