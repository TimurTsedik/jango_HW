from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    current_page = int(request.GET.get('page', 1))

    with open('pagination/data-398-2018-08-30.csv', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        stations = []
        for row in reader:
            stations.append({
                    'Name': row['Name'],
                    'Street': row['Street'],
                    'District': row['District']
            })
    paginator = Paginator(stations, 10)
    current_page = int(request.GET.get('page', 1))
    page = paginator.get_page(current_page)
    context = {
        'bus_stations': page.object_list,
        'page': page,
    }
    return render(request, 'stations/index.html', context)
