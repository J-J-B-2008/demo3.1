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

from . filters import VolareFilter


class HomeListView(ListView):
    model = models.Produtos
    template_name = "home.html"
    context_object_name = "produto"
    ordering = "descricao"
    


def volare(request):
    volareproduto = Produtos.objects.filter(montadora__nome__icontains='volare').order_by('descricao')
    filtro_volare = VolareFilter(request.GET, volareproduto)

    return render(request, 'volare.html', {'volareproduto' : filtro_volare.qs, "filter" : filtro_volare })
