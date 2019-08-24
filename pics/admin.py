from django.contrib import admin
from .models import Image,Place,Category

# Register your models here.

# class ImageAdmin(admin.ModelAdmin):
#     filter_horizontal =('',)

admin.site.register(Image,)
admin.site.register(Place)
admin.site.register(Category)
