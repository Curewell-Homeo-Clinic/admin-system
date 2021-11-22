from django.test import TestCase
from django.contrib.auth.models import User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser',
                                             password='asfasfgadgs')
        self.user.save()

    def test_user_created(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.is_active, True)
        self.assertEqual(self.user.is_staff, False)
        self.assertEqual(self.user.is_superuser, False)
        self.assertEqual(self.user.is_authenticated, True)
        self.assertEqual(self.user.email, '')
        self.assertEqual(self.user.check_password('asfasfgadgs'), True)
        self.assertEqual(self.user.check_password('asfasasdasfgadg'), False)
        self.assertEqual(self.user.groups.count(), 0)

        self.user.delete()
