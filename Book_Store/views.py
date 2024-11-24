from django.shortcuts import render


# Create your views here.

# Home Page View
def home(request):
    return render(request, 'base.html')