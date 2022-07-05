from django.db import models

status_choice = (
    ('d', 'Draft'),
    ('p', 'published'),
)


class Tags(models.Model):
    slug = models.SlugField(unique=True)
    tag_name = models.CharField(max_length=10)

    def __str__(self):
        return self.tag_name


class News(models.Model):
    name = models.CharField(max_length=200, unique=True)
    context = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=status_choice, max_length=2, default='d')
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'News'
        verbose_name = 'News'
        db_table = 'News'
        ordering = ['created_at']

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    user_name = models.CharField(max_length=200)
    comment = models.TextField()
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self) -> str:
        if len(self.comment) > 50:
            return 'Comment {}  by >>>>{}'.format(self.comment[:50], self.user_name)
        else:
            return 'Comment {} by {}'.format(self.comment, self.user_name)
