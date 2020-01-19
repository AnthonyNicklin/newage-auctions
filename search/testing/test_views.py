from django.test import TestCase, Client


class SearchViewTest(TestCase):
    """ Tests views in search app """

    def test_category_view_returns_correct_template(self):
        response = self.client.get('/search/military')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'category.html')
