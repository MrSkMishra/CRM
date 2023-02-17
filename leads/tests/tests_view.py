from django.test import TestCase
from django.shortcuts import reverse

class LandingPageTest(TestCase):
    def test_status_code(self):
        #TODO Some Sort Of Test
        response = self.client.get(reverse("LandingPageView"))
        print(response.status_code)  # For check the test is passed or failed
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed("landing.html")



        # instead of this run like this


    # def test_template_name(self): Run two another another test cases iis not a good practice instead of this run like this
    #     response = self.client.get(reverse("LandingPageView"))
    #     self.assertTemplateUsed(response,"landing.html")