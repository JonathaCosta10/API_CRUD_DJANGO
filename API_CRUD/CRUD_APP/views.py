from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
import json
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist


@csrf_exempt
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


@csrf_exempt
def read_item(request):
    if request.method == 'GET':
        item_id = request.GET.get('id')
        try:
            item = Item.objects.get(pk=item_id)
            return JsonResponse({'success': True, 'item': {'id': item.id, 'name': item.name, 'description': item.description, 'price': float(item.price)}})
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item não encontrado'}, status=404)
    else:
        return JsonResponse({'error está entrando aqui ?': 'Método não permitido', }, status=405)





@csrf_exempt
def create_item(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        try:
            new_item = Item.objects.create(name=name, description=description, price=price)
            return JsonResponse({'success': True, 'message': 'Item criado com sucesso!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'error': 'Método não permitido'}, status=405)



    
@csrf_exempt
def update_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        try:
            item = Item.objects.get(pk=item_id)
            item.name = data.get('name')
            item.description = data.get('description')
            item.price = data.get('price')
            item.save()
            return JsonResponse({'success': True, 'message': 'Item atualizado com sucesso!'})
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item não encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)


@csrf_exempt
def delete_item(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        try:
            item = Item.objects.get(pk=item_id)
            item.delete()
            return JsonResponse({'success': True, 'message': 'Item deletado com sucesso!'})
        except ObjectDoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item não encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)
