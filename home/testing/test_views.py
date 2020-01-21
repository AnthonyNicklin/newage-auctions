from django.test import TestCase


class HomeViewTest(TestCase):
    """ Tests views in home app """

    def test_index_view_returns_correct_template(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

