from django.test import TestCase
from django.urls import reverse 


class AbodeViewTest(TestCase):
    """
    Test for the main views of the abode app.
    """
    def test_landing_page_view_exists(self):
        """
        Ensure the landing page view is accessible and return a 200 status code.
        """
        response = self.client.get(reverse('abode:home'))
        self.assertEqual(response.status_code, 200)

    def  test_landing_page_uses_correct_template(self):
        """
        Ensure the landing page view uses the correct tamplate file
        """
        response = self.client.get(reverse('abode:home'))
        self.assertTemplateUsed(response, 'abode/home.html')