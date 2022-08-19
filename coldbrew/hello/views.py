from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def hello(request):
    return JsonResponse({'text': 'hello, world'}, safe=False)

def index(request):
    return render(request, 'hello/index.html')
