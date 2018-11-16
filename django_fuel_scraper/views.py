from django.shortcuts import render
from django.http import HttpResponse
from fuel_scraper import fuel_day, by_price, create_fuel_table

"""def index(request):
    return render(request, 'index.html', {
        'num' : [1,2,3]
    })"""

def index(request):
    html_data = create_fuel_table()
    return HttpResponse(html_data)

def data(request):
    html_data = create_fuel_table()
    return HttpResponse(html_data)

