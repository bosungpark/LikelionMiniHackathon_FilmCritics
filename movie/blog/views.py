from django.shortcuts import get_object_or_404, render , redirect
from requests.api import get
from .models import Movies
from django.core.paginator import Paginator
import requests
# Create your views here.
def home(request):
    init_db(request)
    blogs= Movies.objects.all()
    query= request.GET.get('query')
    if query:
        blogs= Movies.objects.filter(title_kor__icontains=query)

    paginator= Paginator(blogs, 3)
    page= request.GET.get('page')
    paginated_blogs= paginator.get_page(page)
    return render(request, 'home.html', {'blogs': paginated_blogs})


def init_db(request):
    url = "http://3.36.240.145:3479/mutsa"
    res = requests.get(url)
    movies = res.json()['movies']
    for movie in movies:
        new_movie = Movies()
        new_movie.title_kor = movie['title_kor']
        new_movie.title_eng = movie['title_eng']
        new_movie.poster_url = movie['poster_url']
        new_movie.rating_aud = movie['rating_aud']
        new_movie.rating_cri = movie['rating_cri']
        new_movie.rating_net = movie['rating_net']
        new_movie.genre = movie['genre']
        new_movie.showtimes = movie['showtimes']
        new_movie.release_date = movie['release_date']
        new_movie.rate = movie['rate']
        new_movie.summary = movie['summary']

        for stf in movie['staff']:
            new_stf = Movies.Staff()
            new_stf.name = stf['name']
            new_stf.role = stf['role']
            new_stf.image_url = stf['image_url']
        
        new_movie.save()

        
    return redirect('home')

def detail(request, id):
    blog = get_object_or_404(Movies, pk=id)
    return render(request, 'detail.html', {'blog':blog})
