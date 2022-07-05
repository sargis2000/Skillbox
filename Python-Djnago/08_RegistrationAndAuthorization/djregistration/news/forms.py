
from django import forms
from .models import News, Comment, Tags


class CreateTage(forms.Form):
    class Meta:
        model = Tags
        fields = ['tag_name', 'slug']


class CreateNewsForm(forms.Form):
    name = forms.CharField(max_length=100)
    context = forms.CharField(widget=forms.Textarea)
    tag = forms.CharField(max_length=100)


class CommentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.is_authenticated = kwargs.pop('is_authenticated')
        super().__init__(*args, **kwargs)
        if self.is_authenticated:
            del self.fields['user_name']

    user_name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)


class PublishNews(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.news = News.objects.all()
        for i in self.news:
            field_name = f'NEWS  {i.name}  {i.context[:20] + "..."}  No.{i.id}'
            self.fields[field_name] = forms.BooleanField(required=False)


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)