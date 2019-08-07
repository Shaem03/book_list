from django.conf.urls import include, url
from booksManagement.views import HomePage
from booksManagement.book_list import BookList
from django.urls import path


urlpatterns = [
    url(r'^$', HomePage.home, name="list"),
    url(r'^signup', HomePage.signup, name="signup"),
    url(r'^login', HomePage.login, name="login"),
    url(r'^logout', HomePage.logout, name="logout"),

    url(r'^list', BookList.list, name="list"),
    url(r'^book_edit', BookList.book_edit, name="book_edit"),
    url(r'^edit', BookList.edit, name="edit"),

]