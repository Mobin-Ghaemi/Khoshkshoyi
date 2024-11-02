from django.shortcuts import render, redirect, get_object_or_404
from product import models
# Create your views here.
def home(request):
    search_id = request.GET.get('search_id')
    open = models.Open.objects.get(shomare=1)
    if search_id:
        try:
            sefaresh_item = get_object_or_404(models.sefaresh, id=search_id)
            return redirect('product:sefaresh', id=sefaresh_item.id)
        except models.sefaresh.DoesNotExist:
            ctx = {'error_message': 'چنین شماره سفارشی وجود ندارد'}
            return render(request, 'home.html', ctx)
    return render(request, 'home.html',{'open':open})
def custom_404_view(request, exception):
    return render(request, '404.html', status=404)