from django.urls import path

from . import views

urlpatterns = [
    path('', views.technologies, name='technologies'),
    path('search', views.search, name='search')
]