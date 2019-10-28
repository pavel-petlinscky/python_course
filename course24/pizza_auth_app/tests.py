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

    def test_incorrect_login(self):
        with self.assertNumQueries(2):
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

    def test_correct_login(self):
        with self.assertTemplateUsed(template_name='auth_app/login.html'):
            url = reverse('auth_app:login')
            response = self.client.post(url, {
                'username': self.user.username,
                'password': 'test',
            }, follow=True)


        self.assertEqual(Session.objects.all().count(), 1)

    # def test_correct_login(self):
    #     with self.assertTemplateUsed(template_name='auth_app/login.html'):
    #         url = reverse('auth_app:login')
    #         response = self.client.post(url, {
    #             'username':self.user.username,
    #             'password': self.user.password
    #         }, follow=True)
    #
    #     self.assertTemplateUsed(response, template_name='pizza_app/_base.html')
    #     # self.assertEqual(self.user.is_authenticated, True)
    #     self.assertEqual(Session.objects.all().count(), 1)
    #     self.assertEqual(self.user.is_authenticated, True)


# TODO: add tests for correct login
# TODO: add tests for registration
