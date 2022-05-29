import json
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product

# Create your views here.
def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # Convert model instance to json
        data = model_to_dict(model_data, fields=['id','title'])
    return JsonResponse(data)
