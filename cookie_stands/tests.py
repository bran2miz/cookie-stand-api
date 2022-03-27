from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import CookieStand

class CookieStandTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='admin', password='Brandon14')
        testuser1.save()

        test_cookie_stand = CookieStand.objects.create(location='Paris', owner=testuser1,description='Paris cookies.',)
        test_cookie_stand.save()

    def test_things_model(self):
        cookie_stand = CookieStand.objects.get(id=1)
        actual_owner = str(cookie_stand.owner)
        actual_location = str(cookie_stand.location)
        actual_description = str(cookie_stand.description)
        self.assertEqual(actual_owner,'admin')
        self.assertEqual(actual_location, 'Paris')
        self.assertEqual(actual_description,'Paris cookies.')

