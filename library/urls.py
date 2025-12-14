from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.home, name='home'),           # homepage
    path('books/', views.book_list, name='book_list'),
    path('issue/', views.issue_book, name='issue_book'),
    path('my-books/', views.my_books, name='my_books'),
    path('return/<int:issue_id>/', views.return_book, name='return_book'),

]
