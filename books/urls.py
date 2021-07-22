from django.urls import path
from books.views import catalog, book_page

app_name = 'books'

urlpatterns = [
    path('', catalog, name='index'),
    path('book', book_page, name='book'),
]
