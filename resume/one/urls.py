from django.urls import path

from resume.one import views

urlpatterns = [
    path('', views.resume_view, name='resume'),
]