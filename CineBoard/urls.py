from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/movie_list/', views.MovieListView.as_view(), name='movie_list'),
    path('movies/create_film/', views.MovieCreateView.as_view(), name='create_film'),
    path('movies/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movies/<int:pk>/update_film/', views.MovieUpdateView.as_view(), name='movie_edit'),
    path('movies/<int:pk>/confirm_delete/', views.MovieDeleteView.as_view(), name='movie_delete'),
    path('movies/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('user_list/', views.UserListView.as_view(), name='user_list'),
]
