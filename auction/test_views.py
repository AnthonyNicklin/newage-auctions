from django.test import TestCase

from .models import Lot

class LotViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Lot.objects.create(id=1, name='Tommy Gun', origin='USA', 
            description="Gun used by gangsters in the 50's", age=50, category='MIL')
           
    def test_view_url_exists_at_desired_location(self):
        lot_obj = Lot.objects.get(id=1)

        response = self.client.get('/auctions/lot/{0}/'.format(lot_obj.id), follow=True)
        self.assertEqual(response.status_code, 200)
    