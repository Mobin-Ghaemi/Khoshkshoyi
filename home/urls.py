from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static



app_name ='home'

urlpatterns = [
    path('',views.home,name='home')
]
if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)