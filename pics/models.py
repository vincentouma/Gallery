from django.db import models
from datetime import datetime as dt
# Create your models here.


class Place(models.Model):
    place = models.CharField(max_length = 30)

    def __str__(self):
        return self.place

    def save_place(self):
        self.save()

    def delete_place(self):
        self.delete()

class Category(models.Model):
    category = models.CharField(max_length = 30)



    def __str__(self):
        return self.category


class Picture(models.Model):
    picture = models.ImageField(upload_to='picture/',default='DEFAULT VALUE')
    name = models.CharField(max_length=60)
    details = models.TextField()
    category = models.ForeignKey(Category)
    place = models.ForeignKey(Place)
    pub_date = models.DateTimeField(auto_now_add=True)


    

    def save_picture(self):
        self.save()

    @classmethod
    def todays_picture(cls):
        today = dt.today()
        picture = cls.objects.filter(pub_date__date = today)
        return picture

    @classmethod
    def search_by_category(cls,search_term):
        picture = cls.objects.filter(category__category__icontains=search_term)
        return picture

    @classmethod
    def pics(cls):
        pictures = cls.objects.all()
        return pictures    