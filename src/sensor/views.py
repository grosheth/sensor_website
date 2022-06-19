from django.http import HttpResponse
from .sensors import main


def stats(request):

    main()

    return HttpResponse("<h1>Temparature and humidity")

