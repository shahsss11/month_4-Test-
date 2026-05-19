from django.shortcuts import redirect ,get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views import generic
from django.urls import reverse
from . import models, forms
from django.contrib.auth.models import User


class RegisterView(generic.CreateView):
    template_name = 'users/register.html'
    form_class = forms.UserCreationForm 
    success_url = '/login/'


class LoginView(generic.FormView):
    template_name = 'users/login.html'
    form_class = AuthenticationForm
    success_url = '/user_list/'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)


class LogoutView(generic.View):
    def get(self, request):
        logout(request)
        return redirect('/login/')


class UserListView(generic.ListView):
    template_name = 'users/user_list.html'
    context_object_name = 'users'
    model = models.User


class MovieCreateView(generic.CreateView):
    model = models.Movie
    form_class = forms.MovieForm
    template_name = 'movies/create_film.html'

    def get_success_url(self):
        return reverse('movie_list')

class MovieUpdateView(generic.UpdateView):
    model = models.Movie
    form_class = forms.MovieForm
    template_name = 'movies/update_film.html'

    def get_success_url(self):
        return reverse('movie_list')


class MovieDeleteView(generic.DeleteView):
    model = models.Movie
    template_name = 'movies/movie_confirm_delete.html'

    def get_success_url(self):
        return reverse('movie_list')
    

class MovieListView(generic.ListView):
    template_name = 'movies/movie_list.html'
    context_object_name = 'page_obj'
    model = models.Movie
    paginate_by = 3

    def get_queryset(self):
        search = self.request.GET.get('search', '')
        movies = self.model.objects.all()
        if search:
            movies = movies.filter(title__icontains=search)
        return movies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('search', '')
        return context

class MovieDetailView(generic.DetailView):
    template_name = 'movies/movie_detail.html'
    context_object_name = 'movie'
    model = models.Movie

class AddCommentView(generic.View):
    def post(self, request, pk):
        movie = get_object_or_404(models.Movie, pk=pk)

        form = forms.CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.movie = movie
            comment.save()

        return redirect('movie_detail', pk=pk)