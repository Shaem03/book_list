from django.conf.urls import include, url
from booksManagement.views import HomePage
from booksManagement.book_list import BookList
from django.urls import path
from . import views


urlpatterns = [
    url(r'^$', HomePage.login, name="login"),
    url(r'^signup', HomePage.signup, name="signup"),
    url(r'^login', HomePage.login, name="login"),
    url(r'^logout', HomePage.logout, name="logout"),

    url(r'^list', BookList.list, name="list"),
    url(r'^book_edit', BookList.book_edit, name="book_edit"),
    url(r'^edit', BookList.edit, name="edit"),
    url(r'^book_delete', BookList.book_delete, name="book_delete"),

    path('', views.BooksList.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
]