from django.contrib import admin

# Register your models here.
from tables.models import userbio,contactformdata

class userAdmin(admin.ModelAdmin):
    list_display=['name','mobile','email']

admin.site.register(userbio,userAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display=['name','contact','email','message']

admin.site.register(contactformdata,contactAdmin)


