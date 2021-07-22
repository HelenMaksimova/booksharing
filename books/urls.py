from django.urls import path
from books.views import CatalogListView, book_page

app_name = 'books'

urlpatterns = [
    path('', CatalogListView.as_view(), name='index'),
    path('<int:category_id>/', CatalogListView.as_view(), name='category_filter'),
    path('book/', book_page, name='book'),
]
