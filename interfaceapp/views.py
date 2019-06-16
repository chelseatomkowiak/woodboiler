from django.http import HttpResponse
from django.shortcuts import render

from .models import CurrentStats

def temp_records(request):
    tempp = CurrentStats.objects.all()
    return render(request, 'interfaceapp/temperature.html', {'tempp': tempp})
