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
    # Recuperar e exibir informações sobre um item específico
    pass

@csrf_exempt
def update_item(request, item_id):
    # Processar solicitação PUT para atualizar um item existente
    pass

@csrf_exempt
def delete_item(request, item_id):
    # Processar solicitação DELETE para excluir um item
    pass
