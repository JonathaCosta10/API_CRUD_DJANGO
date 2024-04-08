from django.shortcuts import render
from django.http import JsonResponse
from .models import Item
import json
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render
from .models import Item

@csrf_exempt
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


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
def read_item(request, item_id):
    if request.method == 'GET':
        try:
            item = Item.objects.get(id=item_id)
            return JsonResponse({'success': True, 'item': {
                'id': item.id,
                'name': item.name,
                'description': item.description,
                'price': str(item.price)
            }})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def update_item(request, item_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            item = Item.objects.get(id=item_id)
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            item.price = data.get('price', item.price)
            item.save()
            return JsonResponse({'success': True, 'message': 'Item updated successfully'})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def delete_item(request, item_id):
    if request.method == 'DELETE':
        try:
            item = Item.objects.get(id=item_id)
            item.delete()
            return JsonResponse({'success': True, 'message': 'Item deleted successfully'})
        except Item.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Item not found'}, status=404)
    return JsonResponse({'error': 'Method not allowed'}, status=405)