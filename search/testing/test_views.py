from django.test import TestCase


class SearchViewTest(TestCase):
    """ Tests views in search app """
    
    def test_search_lots_view_returns_correct_template(self):
        response = self.client.get('/search/lots?q=watch')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lot_items.html')
    
    def test_search_auctions_view_returns_correct_template(self):
        response = self.client.get('/search/auctions?q=watch')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auctions.html')

    def test_category_view_returns_correct_template(self):
        response = self.client.get('/search/military')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')
