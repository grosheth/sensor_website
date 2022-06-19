from .sensors import main
from django.shortcuts import render
from datetime import datetime


def stats(request):

    try:
        results = main()
        temperature_c = results[0]
        humidity = results[1]
    except:
        temperature_c = "23.5"
        humidity = "42.4"
        
    return render(request, "index.html", context={"date": datetime.today(), "temperature": temperature_c, "humidity": humidity})

