from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    file_name = settings.BUS_STATION_CSV

    with open(file_name, encoding='utf-8') as file:
        bus_stations = list(csv.DictReader(file))

        paginator = Paginator(bus_stations, 10)
        page_number = int(request.GET.get('page', 1))
        page = paginator.get_page(page_number)
        context = {

                'page': page,
        }
    return render(request, 'index.html', context)


