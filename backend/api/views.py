import json
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    print(request.GET)
    print(request.POST)
    body = request.body
    data = {}
    
    try:
        data = json.loads(body)
    except:
        pass
    
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    
    return JsonResponse(data)
