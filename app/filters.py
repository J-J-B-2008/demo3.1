import django_filters

from app.models import Produtos
from volare.models import GrupoVolare



class VolareFilter(django_filters.FilterSet):

    grupovolare = django_filters.ModelChoiceFilter(
        queryset=GrupoVolare.objects.all().order_by('nome'),
        label='GRUPO',
       
    )

    class Meta:
        model = Produtos
        fields = {
            "descricao": ["icontains"],
            "aplicacao": ["icontains"],            
        }