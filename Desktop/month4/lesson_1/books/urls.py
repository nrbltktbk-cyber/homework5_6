from django.urls import path
from books.views import BookListView, BookDetailView, SearchView
app_name='knigi'

urlpatterns = [
    path('', BookListView.as_view(), name='books' ),
    path('books/<int:id>/', BookDetailView.as_view()),
    path('search/', SearchView.as_view()),
]