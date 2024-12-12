from django.contrib import admin
from .models import Staff, Author, Book, Customer, Transaction # importing the models from the models.py file

# Register your models here.
# This is where you register your models to be displayed on the admin page

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'picture')
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'isbn', 'stock', 'published_date')
    list_filter = ('category', 'author')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'isbn') 
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'chosen_username', 'email', 'phone', 'address', 'city', 'state', 'zip')



