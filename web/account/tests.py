from django.contrib.auth.models import User
from django.test import TestCase

from .models import Profile

class ProfileTests(TestCase):

    def setUp(self):
        email='test@email.com'
        self.user = User.objects.create(username=email, email=email)


    def test_user_creation_creates_profile(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())


    def test_profile_unchanged_on_second_user_save(self):
        p = self.user.profile
        p.full_name = 'Joe Schmoe'
        p.save()
        self.user.username = 'joeschmoe'
        self.user.save()
        self.assertEquals(p.full_name, 'Joe Schmoe')
