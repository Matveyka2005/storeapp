from django.test import TestCase
from films.models import Film, Category


image = 'image.jpg'
video = 'video.mp4'

class TestModels(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name="comedy",
            )

        self.film1 = Film.objects.create(
            name="testname",
            about="a about here",
            image=image,
            video=video,
            author="Author1",
            category=self.category
        )
     
    def test(self):
        #print(self.category.film_set.get(pk=1).about)
        self.assertEqual(self.category.name, "comedy")
