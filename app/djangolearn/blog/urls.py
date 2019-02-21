from django.urls import path

from .views import *

# some-title

urlpatterns = [
    path('', posts_list)
]