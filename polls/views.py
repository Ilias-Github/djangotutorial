# View is the interface that accepts user interaction. It takes a web request and returns a web response
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")