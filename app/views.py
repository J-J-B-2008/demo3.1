from django.db.models.query import QuerySet
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.shortcuts import render
from app.models import Produtos
from django.views import View
from grupo.models import Group
from app.models import Grupo
from typing import Any
from . import models


class HomeListView(ListView):
    model = models.Produtos
    template_name = "home.html"
    context_object_name = "produto"
    ordering = "descricao"
    


class VolareListView(ListView):
    model = models.Produtos
    template_name = "volare.html"
    context_object_name = "volareproduto"
    ordering = "descricao"
    

    def get_queryset(self):
        volareproduto = super().get_queryset()              
        search = self.request.GET.get('search')
        grupo = self.request.GET.get('grupo')
        volareproduto = Produtos.objects.filter(montadora__nome__icontains='volare').order_by('descricao')

        if search:
            volareproduto = Produtos.objects.filter(aplicacao__icontains=search)  

        if grupo:
            volareproduto = Produtos.objects.filter(grupo__id=grupo)

        return volareproduto 
        
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['grupos'] = Group.objects.all().order_by('nome')
          

        return context  
