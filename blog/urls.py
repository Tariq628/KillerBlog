from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name="blogHome"),
    path("contact/", views.contact, name="contact"),
    path("search/", views.search, name="search"),
    path("blogpost/", views.blogpost, name="blogpost")
]
