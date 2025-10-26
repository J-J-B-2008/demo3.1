from django.urls import path
from . import views


urlpatterns = [
    path('grupo/', views.GrupoListView.as_view(), name="grupo_list"),


] 
