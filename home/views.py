from django.shortcuts import render
from product import models
# Create your views here.
def home(request):
    try:
        open = models.Open.objects.get(shomare=1)
    except models.Open.DoesNotExist:
        open = None  

    ctx = {
        'open': open,
    }
    print(ctx)
    return render(request, 'home.html', ctx)