from django.db import models
from datetime import datetime as dt
# Create your models here.


class Place(models.Model):
    location = models.CharField(max_length = 30)

    def __str__(self):
        return self.location

    def save_place(self):
        self.save()

    def delete_place(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length = 30)



    def __str__(self):
        return self.category


class Image(models.Model):
    image_name = models.CharField(max_length= 30)
    image_description = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'gallery/', default = "")
    image_location = models.ForeignKey(
        Place,
        on_delete=models.DO_NOTHING)
    image_category = models.ForeignKey(
        Category,
        on_delete = models.DO_NOTHING)

    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image_name

# Create your models here.
