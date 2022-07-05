from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from blog.forms import BlogForm


class BlogFormTestCase(TestCase):
    def setUp(self) -> None:
        self.image = SimpleUploadedFile(name='file_example_JPG_500kB.jpg',
                                        content=open('/home/sargis/Pictures/file_example_JPG_500kB.jpg', 'rb').read(),
                                        content_type='image/jpg')

    def test_valid_form(self) -> None:
        form = BlogForm(data={'title': 'anytitle', 'content': 'adnasd'}, files={'images': self.image})
        print(form.errors)
        self.assertTrue(form.is_valid())