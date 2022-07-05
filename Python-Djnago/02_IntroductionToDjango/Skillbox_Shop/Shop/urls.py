from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cours1', views.courses, {'name': 'Course1'}, name='CourseView1'),
    path('cours2', views.courses, {'name': 'Course2'}, name='CourseView2'),
    path('cours3', views.courses, {'name': 'Course3'}, name='CourseView3'),
    path('cours4', views.courses, {'name': 'Course4'}, name='CourseView4'),
]
