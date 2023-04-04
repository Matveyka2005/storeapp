from django.shortcuts import render
from django.views import generic

from .service import all_objects, all_objects_by_select_related, single_obj_or_single_and_select_related, filter_objects
from films.models import Film, Category
from .forms import FilmForm


class MainPageListView(generic.ListView):
    model = Film
    template_name = 'films/home.html'
    context_object_name = 'films'
    
    def get_queryset(self):
        return Film.objects.select_related('category').all()
    
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = Category.objects.all()
        return data 
    

def film_detail(request, film_id):
    film = Film.objects.select_related('category').get(pk=film_id)
    data = {
        "films": film,
    }
    return render(request, 'films/detail_film.html', context=data)


def filter_films_by_category(request, cat_id):
    categories = all_objects(Category)
    films = Film.objects.filter(category=cat_id)
    data = {
        "categories": categories,
        "films": films,
    }
    return render(request, 'films/home.html', context=data)


class CreateFilm(generic.CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'films/create.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['categories'] = all_objects(Category)
        return data

    def form_valid(self, form):
        return super().form_valid(form)
    


