from django.urls import path
from .views import books_list, books_manage

from .views import (
    ProtectedBooksView,
    ManageBooksView,
    CustomScopeBooksView,
    ClientProtectedBooksView
)

from .views import OIDCBooksView, OIDCLogoutView

urlpatterns = [
    path("books/", books_list, name="books-list"),
    path("books/manage/", books_manage, name="books-manage"),
    path("cbv/books/", ProtectedBooksView.as_view(), name="cbv-books"),
    path("cbv/books/manage/", ManageBooksView.as_view(), name="cbv-books-manage"),
    path("cbv/books/scope/", CustomScopeBooksView.as_view(), name="cbv-books-scope"),
    path("cbv/books/client/", ClientProtectedBooksView.as_view(), name="cbv-books-client"),
    path("oidc/books/", OIDCBooksView.as_view(), name="oidc-books"),
    path("oidc/logout/", OIDCLogoutView.as_view(), name="oidc-logout"),
]