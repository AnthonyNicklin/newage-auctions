from django.test import TestCase

from auction.models import Lot


class LotModelTest(TestCase):
    @classmethod
    # Set up non-modified objects used by all test methods
    def setUpTestData(cls):
        Lot.objects.create(id=1, name='Tommy Gun', origin='USA', 
            description="Gun used by gangsters in the 50's", age=50, category='military')

    def test_name_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_name_max_length(self):
        lot_obj = Lot.objects.get(id=1)
        max_length = lot_obj._meta.get_field('name').max_length
        self.assertEquals(max_length, 200)

    def test_origin_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('origin').verbose_name
        self.assertEquals(field_label, 'origin')

    def test_origin_max_length(self):
        lot_obj = Lot.objects.get(id=1)
        max_length = lot_obj._meta.get_field('origin').max_length
        self.assertEquals(max_length, 200)

    def test_description_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')
    
    def test_age_label(self):
        lot_obj = Lot.objects.get(id=1)
        field_label = lot_obj._meta.get_field('age').verbose_name
        self.assertEquals(field_label, 'age')

    

