from django.contrib import admin

# Register your models here.
from .models import CustomUser

class CustumUserAdmin(admin.ModelAdmin):
    list_display = ('id','username')
    list_display_links = ('id','username')

admin.site.register(CustomUser,CustumUserAdmin)