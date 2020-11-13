from django.http import HttpResponse
from datetime import datetime

def index(request):
    # now = datetime.now().strftime('%b %dth, %Y - % H:%M hrs')
    return HttpResponse('La Fecha es: {now}'.format(
        now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def hi(request):
    print(request)
    return HttpResponse("request")