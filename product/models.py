from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class sefaresh (models.Model):
    vaziatchoises={
       ('0','تحویل گرفته شد'),
       ('1','اماده ی تحویل'),

    }
    name =models.CharField(max_length=80,verbose_name='نام و نام خانوادگی')
    shomare= models.BigIntegerField(verbose_name='شماره تماس ')
    created =jmodels.jDateField(auto_now=True,verbose_name='تاریخ سفارش')
    vaziat = models.CharField(max_length=30,verbose_name='وضعیت سفارش :',default='0',choices=vaziatchoises,)

class Open(models.Model):
    openchoises ={
        ('باز','باز'),
        ('بسته','بسته'),
    }
    open=models.CharField(max_length=25,verbose_name='وضعیت باز بودن : ',choices=openchoises)
    shomare =models.IntegerField()
    def __str__(self) -> str:
        return self.open