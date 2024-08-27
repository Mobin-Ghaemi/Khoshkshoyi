from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class sefaresh (models.Model):
    name =models.CharField(max_length=80,verbose_name='نام و نام خانوادگی')
    shomare= models.BigIntegerField(verbose_name='شماره تماس ')
    created =jmodels.jDateField(auto_now=True,verbose_name='تاریخ سفارش')

