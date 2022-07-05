from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from login_register.forms import NewUserForm


class BlogFormTestCase(TestCase):

    def test_invalid_form(self) -> None:
        form = NewUserForm(data={"username": 'saqo', "email": 'khachatryansargis200kh@gmail.com',
                                 "password1": 'Arm220@a', "password2": 'Arm2020@a'})

        self.assertFalse(form.is_valid())

    def test_valid_form(self) -> None:
        form = NewUserForm(data={"username": 'saqo', "email": 'khachatryansargis200kh@gmail.com',
                                 "password1": 'Arm2020@a', "password2": 'Arm2020@a'})

        self.assertTrue(form.is_valid())