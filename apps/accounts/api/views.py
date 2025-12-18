from django.http import HttpResponse

def home(request):
    return HttpResponse('Hi, this is accounts section!')