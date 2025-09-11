from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("I am MlOps Engineer, I like Docker!")
