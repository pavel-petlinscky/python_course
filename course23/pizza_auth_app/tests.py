from django.test import TestCase, Client
from django.urls import reverse

from django.contrib.sessions.models import Session

from pizza_auth_app.models import CustomUser


class TestLoginView(TestCase):

    @classmethod
    def setUp(cls):
        cls.password = 'test'
        cls.user = CustomUser(
            username='test',
            email='test@mail.com'
        )
        cls.user.set_password(cls.password)
        cls.user.save()

        cls.client = Client()

    def tearDown(self):
        print('TEAR DOWN')

    @classmethod
    def tearDownClass(cls):
        print('AFTER ALL TESTS')

    def test_list(self):
        class A:
            def __init__(self, a):
                self.a = a

            def __eq__(self, other):
                return self.a == other.a

        x = A(1)
        y = A(1)
        a = [1, x]
        b = [1, y]
        self.assertNotEqual(id(x), id(y))
        self.assertListEqual(a, b)

    def test_incorrect_login(self):
        with self.assertNumQueries(1):
            with self.assertTemplateUsed(template_name='auth_app/login.html'):
                url = reverse('auth_app:login')
                response = self.client.post(url, {
                    'username': self.user.username,
                    'password': 'wrong-password',
                }, follow=True)

        self.assertTemplateUsed(response, template_name='pizza_app/_base.html')
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            'Please enter a correct username and password',
            str(response.content)
        )
        self.assertContains(response, 'Please enter a correct username and password')
        self.assertFormError(response, form='form',
                             field=None,
                             errors='Please enter a correct username and password. Note that both fields may be case-sensitive.')
        self.assertEqual(Session.objects.all().count(), 0)


# TODO: add tests for correct login
# TODO: add tests for registration
