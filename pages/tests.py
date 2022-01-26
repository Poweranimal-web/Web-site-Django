from django.test import SimpleTestCase

class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertAlmostEqual(response.status_code,200)
    def tes_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertAlmostEqual(response.status_code, 200)
