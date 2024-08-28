from django.urls import path
from product import views

app_name ='product'

urlpatterns = [
    path('sabt',views.sabteSefaresh,name='sabt'),
    path('success/<int:object_id>',views.movafagh,name='success'),
]
