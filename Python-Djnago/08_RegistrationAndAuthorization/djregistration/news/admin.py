from django.contrib import admin
from .models import *


@admin.action(description="Mark selected Items as published")
def make_published(self, request, queryset) -> None:
    queryset.update(status='p')
    self.message_user(request, "successfully marked as published.")


@admin.action(description="Mark selected Items as draft", )
def make_draft(self, request, queryset) -> None:
    queryset.update(status='d')
    self.message_user(request, "successfully marked as draft.")


class NewsInline(admin.TabularInline):
    model = Comment
    extra = 5


@admin.register(Comment)
class DecoratedCommentAdmin(admin.ModelAdmin):
    def delete_comments(self, request, queryset) -> None:
        queryset.update(comment='Удалено администратором')
        self.message_user(request, 'successfully deleted')

    @staticmethod
    def short_comment(comment: Comment) -> str:
        return comment.comment[:15] + '...'

    list_display = ['user_name', 'news', 'created_on', 'short_comment']
    list_filter = ['user_name']
    actions = [delete_comments]


@admin.register(News)
class DecoratedNewsAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at', 'status']
    list_filter = ['status']
    inlines = [NewsInline]
    actions = [make_published, make_draft]
