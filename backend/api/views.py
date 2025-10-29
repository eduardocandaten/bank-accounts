import json
from django.http import HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import Account, Transaction

@csrf_exempt
def accounts(request: HttpRequest):
    match request.method:
        case 'GET':
            data = list(Account.objects.values())
            return JsonResponse(data, safe=False)
        
        case 'POST':
            body = json.loads(request.body.decode('utf-8'))
            account = Account.objects.create(name=body['name'])
            return JsonResponse({
                'id': account.id,
                'name': account.name,
                'balance': account.balance,
                'created_at': account.created_at
            }, status=201)

@csrf_exempt
def transactions(request: HttpRequest):
    match request.method:
        case 'POST':
            body = json.loads(request.body.decode('utf-8'))
            transaction = Transaction.objects.create(
                receiver_id=body['receiver_id'],
                payer_id=body['payer_id'],
                value=body['value']
            )
            return JsonResponse({
                'id': transaction.id,
                'receiver_id': transaction.receiver_id,
                'payer_id': transaction.payer_id,
                'value': transaction.value,
                'date': transaction.date,
            })
