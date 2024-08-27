from django.contrib import admin
from product import models



@admin.register(models.sefaresh)
class SefarshAdmin(admin.ModelAdmin):
    list_display=['name','id','shomare','created']
    search_fields=['name','id','shomare']
    list_filter=['created']