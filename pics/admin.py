from django.contrib import admin
from .models import Picture,Place,Category

# Register your models here.

# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal =('',)

admin.site.register(Picture)
admin.site.register(Place)
admin.site.register(Category)
