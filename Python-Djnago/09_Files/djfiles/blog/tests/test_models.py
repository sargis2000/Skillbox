from django.core.exceptions import ValidationError
from django.test import TestCase
from blog.models import BlogPost,Picture


class BlogPostTestCase(TestCase):
    def test_invalid_title(self):
        self.title = 't' * 501
        self.obj = BlogPost(title=self.title, content='Any content')
        try:
            self.obj.full_clean()
            self.obj.save()
        except ValidationError:
            pass
        else:
            self.fail('Title Max length must be 500')


class PictureTestCase(TestCase):
    def test_valid_foreignkey(self):
        try:
            self.obj = Picture(image='adada/asdasda/asda.jpg', news_id=10)
            self.obj.full_clean()
        except ValidationError:
            pass
        else:
            self.fail('Something with ForeignKey wrong')




