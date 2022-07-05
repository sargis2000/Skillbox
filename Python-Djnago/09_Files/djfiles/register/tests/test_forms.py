from django.test import TestCase
from register.forms import AdditionalInfoForm


class AdditionalInfoFormTestCase(TestCase):

    def test_wrong_values(self):
        self.form = AdditionalInfoForm(data={'first_name': 'sasdd', 'last_name': ''})
        self.assertFalse(self.form.is_valid())
        self.form = AdditionalInfoForm(data={'first_name': 'dfdsf'*200, 'last_name': 'sasdd'})
        self.assertFalse(self.form.is_valid())

