from django.http import HttpResponse
from .initial_ui import initial_ui_page

def packages_home(request):
    return HttpResponse(initial_ui_page)