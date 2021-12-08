from django.conf.urls import url
from first_api_backend import views

urlpatterns = [
    url(r'^$', views.second_page, name = 'second_page'),
]
