from django.views.generic import ListView
from . import models


class GrupoListView(ListView):
    model = models.Group
    template_name = 'group.html'
    context_object_name = 'groups'
    ordering = 'nome'
