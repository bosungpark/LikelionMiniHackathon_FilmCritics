from django.shortcuts import render
from .models import Blog
from django.core.paginator import Paginator
# import requests

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

# def init_db(request):
#     url= "http://3.36.240.145:3479/mutsa"
#     res= requests.get(url)
#     movies=res.json()['movies']
#     for movie in movies:
#         ##
#     return redirect('home')
