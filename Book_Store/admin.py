from django.contrib import admin
from .models import Staff, Author, Book, Customer, Transaction # importing the models from the models.py file

# Register your models here.
# This is where you register your models to be displayed on the admin page

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'picture')
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'isbn', 'stock', 'cover')
    fields = ('title', 'author', 'price', 'isbn', 'stock', 'cover')  
    

admin.site.register(Staff)


admin.site.register(Customer)
# admin.site.register(Transaction)
