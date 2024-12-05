# Book_Store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm
from django.db.models import Q  # For advanced search queries

def home(request):
    return render(request, 'home.html')

def book_list(request):
    books = Book.objects.all()
    
    # Filter books by selected category
    selected_category = request.GET.get('category', '')
    if selected_category:
        books = books.filter(category=selected_category)
    
    # Search books by title or author
    query = request.GET.get('q', '')
    if query:
        books = books.filter(Q(title__icontains=query) | Q(author__icontains=query))
    
    # Sort books by price
    sort_by_price = request.GET.get('sort', '')
    if sort_by_price == 'asc':
        books = books.order_by('price')
    elif sort_by_price == 'desc':
        books = books.order_by('-price')
    
    # Pass the context to the template
    context = {
        'books': books,
        'categories': Book.CATEGORY_CHOICES,
        'selected_category': selected_category,
        'query': query,
        'sort_by_price': sort_by_price,
    }
    return render(request, 'books/book_list.html', context)

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


def book_author_list(request):
    categories = Book.CATEGORY_CHOICES
    selected_category = request.GET.get('category', '')
    sort_by_price = request.GET.get('sort', '')

    if selected_category:
        books = Book.objects.filter(category=selected_category)
        authors = Author.objects.filter(book__in=books).distinct()
    else:
        authors = Author.objects.all()

    context = {
        'authors': authors,
        'categories': categories,
        'selected_category': selected_category,
        'sort_by_price': sort_by_price,
    }
    return render(request, 'books/book_author_list.html', context)

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    books = Book.objects.filter(author=author)
    return render(request, 'books/book_author_detail.html', {'author': author, 'books': books})