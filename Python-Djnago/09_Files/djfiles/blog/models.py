from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.TimeField(auto_now=True)


class Picture(models.Model):
    image = models.ImageField('Picture', upload_to='pictures/%Y%m%d')
    news = models.ForeignKey(BlogPost, on_delete=models.CASCADE)





