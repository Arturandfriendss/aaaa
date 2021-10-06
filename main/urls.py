from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('new_deal/', views.new_deal, name="new_deal"),
    path('one/', views.one, name="one"),
]