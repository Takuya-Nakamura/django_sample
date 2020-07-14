from django.urls import path
from . import views
from .views import ApiView

app_name = 'diary'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('api', ApiView.as_view(), name='index2'),
  path('api_test', views.api_test, name='index2'),

] 