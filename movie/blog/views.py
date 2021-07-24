from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import Paginator
import requests

# Create your views here.
def home(request):
    blogs= Blog.objects.order_by('-pub_date')

    query= request.GET.get('query')
    if query:
        blogs= Blog.objects.filter(title__icontains=query)

    paginator= Paginator(blogs, 3)
    page= request.GET.get('page')
    paginated_blogs= paginator.get_page(page)
    return render(request, 'home.html', {'blogs': paginated_blogs})