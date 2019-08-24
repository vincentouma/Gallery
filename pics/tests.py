from django.test import TestCase
from .models import Image,Place,Category


# Create your tests here.
class ImageTestClass(TestCase):

    def setUp(self):
        self.moringa=Image(image_name = models.CharField(max_length= 30)
    image_description = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'gallery/', default = "")
    image_location = models.ForeignKey(
        Place,
        on_delete=models.DO_NOTHING)
    image_category = models.ForeignKey(
        Category,
        on_delete = models.DO_NOTHING)

    post_date = models.DateTimeField(auto_now_add=True)


)

#test insatance
    def test_instance(self):
        self.assertTrue(isinstance(self.moringa,Image))


    # Testing Save Method
    def test_save_method(self):
        self.moringa.save_image()
        image = Image.objects.all()
        self.assertTrue(len(image) > 0)    