from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.books_list, name="books_list"),
    path("library/<int:id>/", views.library_detail, name="library_detail"),
]
