from django.shortcuts import render
from django.http import HttpResponse

from .models import Vehicle, Service, Reclamation


# Create your views here.
def sandbox(request):
    # return HttpResponse('this is sandbox')
    return render(request, 'main.html')

def view_1(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'view_1.html', {'vehicles': vehicles})


def view_2(request):
    services = Service.objects.all()
    return render(request, 'view_2.html', {'services': services})


def view_3(request):
    reclamations = Reclamation.objects.all()
    return render(request, 'view_3.html', {'reclamations': reclamations})
