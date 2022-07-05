from django import forms

from . models import News, Comment


class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'context', 'status']


class CommentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.is_authenticated = kwargs.pop('is_authenticated')
        super().__init__(*args, **kwargs)
        if self.is_authenticated:
            del self.fields['user_name']

    user_name = forms.CharField()
    comment = forms.CharField(widget=forms.Textarea)
