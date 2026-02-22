from django.urls import path

from one import views

urlpatterns = [
    path('', views.resume_view, name='resume'),
]