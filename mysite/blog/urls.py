from django.urls import path

from mysite.blog.views import home

app_name = 'blog'

urlpatterns = [
    path('', home, name='home'),
]
