from django.contrib import admin

# Register your models here.
from .models import categ, products


class catagdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catagdmin)




class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img']
    list_editable=['price','stock','img']
    prepopulated_fields={'slug':('name',)}
admin.site.register(products,prodAdmin)

