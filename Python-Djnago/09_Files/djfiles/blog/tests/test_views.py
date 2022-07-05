
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile


class BlogViewTestCase(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        self.response = self.c.get(reverse('blog_view'))

    def test_blog_view(self) -> None:
        self.assertTemplateUsed(response=self.response, template_name='blog/blogview.html')
        self.assertEqual(self.response.status_code, 200)


class CreateBlogTestCase(TestCase):
    def setUp(self) -> None:
        User.objects.create_user(username='admin', password='admin')
        self.client.login(username='admin', password='admin')
        self.get_response = self.client.get(reverse('creat_news'))
        self.image = SimpleUploadedFile(name='file_example_JPG_500kB.jpg',
                                        content=open('/home/sargis/Pictures/file_example_JPG_500kB.jpg', 'rb').read(),
                                        content_type='image/jpg')
        self.post_response = self.client.post(reverse('creat_news'), {'title': 'newpost', 'content': 'ankaptext',
                                                                      'images': self.image, },
                                              format='multipart')

    def test_create_blog_authenticated_user(self):
        self.assertTemplateUsed(response=self.get_response, template_name='blog/create_blog.html')
        self.assertRedirects(self.post_response, reverse('blog_view'))
        self.assertEqual(self.get_response.status_code, 200)
        self.assertEqual(self.post_response.status_code, 302)
        self.client.logout()
