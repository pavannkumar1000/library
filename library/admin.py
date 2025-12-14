from django.contrib import admin
from .models import Category, Author, Book, BookIssue


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'category',
        'total_copies',
        'available_copies'
    )
    list_filter = ('category', 'author')
    search_fields = ('title', 'isbn')


@admin.register(BookIssue)
class BookIssueAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'book',
        'issue_date',
        'return_date',
        'is_returned'
    )
    list_filter = ('is_returned',)
