from django.shortcuts import render, redirect, get_object_or_404
from product import models
# Create your views here.
def home(request):
    search_id = request.GET.get('search_id')
    open = models.Open.objects.get(shomare=1)
    if search_id:
        try:
            # Try to get the sefaresh object with the given ID
            sefaresh_item = get_object_or_404(models.sefaresh, id=search_id)
            # Redirect to the sefaresh detail page if found
            return redirect('product:sefaresh', id=sefaresh_item.id)
        except models.sefaresh.DoesNotExist:
            # If no sefaresh found, pass a message to the template
            ctx = {'error_message': 'چنین شماره سفارشی وجود ندارد'}
            return render(request, 'home.html', ctx)
    

    # If no search_id is provided, just render the home page
    return render(request, 'home.html',{'open':open})