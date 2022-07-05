from django.test import TestCase
from django.urls import reverse


class RegisterTestCase(TestCase):

    def test_register_get(self):
        self.response = self.client.get(reverse('register'))
        self.assertTemplateUsed(response=self.response, template_name='registration/register.html')
        self.assertEqual(self.response.status_code, 200)

    def test_register_post_fail(self):
        self.response = self.client.post(
            reverse('register'),
            {'username': 'sdfsdfsd', 'password1': 'AnyValidPass12!', 'password2': 'AnyValidPass13!', }
        )
        self.assertTemplateUsed(response=self.response, template_name='registration/register.html')
        self.assertContains(response=self.response, text='form')
