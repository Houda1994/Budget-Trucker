"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Book_Store import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Root URL pattern for the home page
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in auth URLs
    path('books/', views.book_list, name='book_list'),  # Book list view
    path('books/<int:pk>/', views.book_detail, name='book_detail'), # Book detail view
    path('books-authors/', views.book_author_list, name='book_author_list'), # Author List
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
     path('authors/suggestions/', views.author_suggestions, name='author_suggestions'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)