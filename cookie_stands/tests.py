from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CookieStand

class CookieStandTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='admin', password='Brandon14')
        testuser1.save()

        test_cookie_stand = CookieStand.objects.create(location='Paris', owner=testuser1,description='Paris cookies.', hourly_sales='[40]', minimum_customers_per_hour='20', maximum_customers_per_hour='30', average_cookies_per_sale='20')
        test_cookie_stand.save()

    def test_things_model(self):
        cookie_stand = CookieStand.objects.get(id=1)
        actual_owner = str(cookie_stand.owner)
        actual_location = str(cookie_stand.location)
        actual_description = str(cookie_stand.description)
        actual_hourly_sales = str(cookie_stand.hourly_sales)
        actual_minimum_customers_per_hour = str(cookie_stand.minimum_customers_per_hour)
        actual_maximum_customers_per_hour = str(cookie_stand.maximum_customers_per_hour)
        actual_average_cookies_per_sale = str(cookie_stand.average_cookies_per_sale)
        self.assertEqual(actual_owner,'admin')
        self.assertEqual(actual_location, 'Paris')
        self.assertEqual(actual_description,'Paris cookies.')
        self.assertEqual(actual_hourly_sales, '[40]')
        self.assertEqual(actual_minimum_customers_per_hour, '20')
        self.assertEqual(actual_maximum_customers_per_hour, '30')
        self.assertEqual(actual_average_cookies_per_sale, '20')
