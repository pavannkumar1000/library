from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BookIssue
from .forms import BookIssueForm
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q  



@login_required(login_url='login')
def home(request):
    return render(request, 'library/home.html')



@login_required
def book_list(request):
    query = request.GET.get('q')  # Get search query
    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__name__icontains=query) |
            Q(category__name__icontains=query)
        )
    else:
        books = Book.objects.all()
    
    return render(request, 'library/book_list.html', {'books': books, 'query': query})

@login_required
def issue_book(request):
    if request.method == 'POST':
        form = BookIssueForm(request.POST, user=request.user)
        if form.is_valid():
            # Save the issue record
            issue = form.save(commit=False)
            issue.user = request.user
            issue.save()

            # Update book availability
            book = issue.book
            book.available_copies -= 1
            book.save()

            # Success message
            messages.success(request, f'Book "{book.title}" issued successfully!')
            return redirect('library:my_books')
        else:
            # Show form errors
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = BookIssueForm(user=request.user)

    return render(request, 'library/issue_book.html', {'form': form})

@login_required
def my_books(request):
    issues = BookIssue.objects.filter(
        user=request.user,
        is_returned=False
    )
    return render(request, 'library/my_books.html', {'issues': issues})

@login_required
def return_book(request, issue_id):
    issue = BookIssue.objects.get(id=issue_id, user=request.user)

    if not issue.is_returned:
        issue.is_returned = True
        issue.return_date = timezone.now().date()
        issue.save()

        book = issue.book
        book.available_copies += 1
        book.save()

    return redirect('library:my_books')
