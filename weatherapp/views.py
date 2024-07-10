from django.shortcuts import render,redirect
import requests
import datetime

def index(request):
    if 'city' in request.POST and request.POST['city'].strip():
        city = request.POST['city']
        apikey = 'cc41f160699d00c5047841b2b8a531bc'
        URL = 'https://api.openweathermap.org/data/2.5/weather'
        parameters = {'q': city, 'appid': apikey, 'units': 'metric'}
        
        r = requests.get(url=URL, params=parameters)
        res = r.json()
        
        if r.status_code == 200:
            description = res['weather'][0]['description']
            icon = res['weather'][0]['icon']
            temp = res['main']['temp']
            day = datetime.date.today()
            humidity = res['main']['humidity']
            wind_speed = res['wind']['speed']
            context = {'description': description,'icon': icon,'temp': temp,'day': day,'city': city,'wind_speed': wind_speed,'humidity': humidity,'error': None}
        else:
            context = {'error': 'City not found. Please enter a valid city.'}
    else:
        context = {'error': 'Please enter a Location.'}

    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def terms(request):
    return render(request, 'terms.html')

def privacy(request):
    return render(request, 'privacy.html')

def help(request):
    return render(request, 'help.html')

def support(request):
    return render(request, 'support.html')
