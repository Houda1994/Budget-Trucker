# Book_Store/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import BookForm
from django.db.models import Q  # For advanced search queries
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout

def home(request):
    if request.user.is_authenticated:
        return redirect('book_list')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('book_list')
    else:
        form = AuthenticationForm()
    return render(request, 'home.html', {'form': form})


login_required
def account(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'account.html')

def book_list(request):
    query = request.GET.get('q', '')
    selected_category = request.GET.get('category', '')
    sort_by_price = request.GET.get('sort', '')

    books = Book.objects.all()

    if query:
        books = books.filter(title__icontains=query)

    if selected_category:
        books = books.filter(category=selected_category)

    if sort_by_price == 'asc':
        books = books.order_by('price')
    elif sort_by_price == 'desc':
        books = books.order_by('-price')

    categories = Book.CATEGORY_CHOICES

    context = {
        'books': books,
        'query': query,
        'selected_category': selected_category,
        'sort_by_price': sort_by_price,
        'categories': categories,
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

def author_suggestions(request):
    query = request.GET.get('q', '')
    if query:
        authors = Author.objects.filter(first_name__icontains=query) | Author.objects.filter(last_name__icontains=query)
        suggestions = list(authors.values('pk', 'first_name', 'last_name'))
        return JsonResponse(suggestions, safe=False)
    return JsonResponse([], safe=False)

def about(request):
    return render(request, 'books/about.html')

