from django import forms
from .models import Picture, BlogPost


class BlogForm(forms.Form):
    title = forms.CharField(max_length=500)
    content = forms.CharField(widget=forms.Textarea)
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

    def save(self, request):
        data = self.cleaned_data
        post = BlogPost.objects.create(title=data['title'], content=data['content'])
        print(post)
        if request.FILES:
            for f in request.FILES.getlist('images'):
                Picture.objects.create(image=f, news=post)

