# This is the Database File for the Book Store App
# This file contains the models for the Book Store App
from django.db import models

# Create your models here.

# This is the Author Model
class Author(models.Model):
    authorID = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=1000)
    last_name = models.CharField(max_length=1000)
    dob = models.DateField()
    picture = models.ImageField(upload_to='authors/', blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" or "Unnamed Author"

# This is the Book Model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    isbn = models.CharField(max_length=13)
    stock = models.IntegerField()
    cover = models.ImageField(upload_to='covers/', blank=True)

    def __str__(self):
        return self.title
    

# This is the Customer/User Model
class Customer(models.Model):
    customerID = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    chosen_username = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}" or "Unnamed Customer"

# This is the Transaction Model
class Transaction:
    transactionID = models.AutoField(primary_key=True, null=False)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.transactionID)
    
# this is the staff model
class Staff(models.Model):
    staffID = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    def __str__(self):
        return print(f"Handled by {self.first_name} {self.last_name}")
    
# This is the Role Model
class Role(models.Model):
    roleID = models.AutoField(primary_key=True, null=False)
    role = models.CharField(max_length=100)

    def __str__(self):
        return print(f"{self.role}")

# This is the Publisher Model
class Publisher(models.Model):
    publisherID = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return print(f"Published by {self.name}")
    
