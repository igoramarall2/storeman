from datetime import datetime
import json
from django.http import JsonResponse
from .models import Order, Product

def save_orders(request):
    if request.method == 'POST':
        # Parse JSON data from the request body
        data = json.loads(request.body.decode('utf-8'))
        
        # Retrieve cliente and produtos from the parsed JSON data
        cliente = data.get('cliente')
        produtos = data.get('produtos')
        
        # Create a new order instance and save it
        order = Order(client_id=cliente)
        order.date = datetime.now()
        order.save()

        total_price = 0
        #TODO: REMOVER DA TABELA DE PRODUTOS A QUANTIDADE DE PRODUTOS VENDIDOS
        for produto in produtos:
            produto_id = produto['id']
            quantity = produto['quantity']
            product = Product.objects.get(id=produto_id)            
            order.products.add(product, through_defaults={'quantity': quantity})
            total_price += product.priceprod * quantity
            order.total = total_price
            product.avprod = product.avprod - quantity
            product.save()
            order.save()
        
        # Return a JsonResponse if needed
        return JsonResponse({'cliente': cliente, 'produtos': produtos})
    
    # Handle other HTTP methods if necessary
    return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)