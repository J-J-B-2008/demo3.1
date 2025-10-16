from django.shortcuts import render
from app.models import Produtos

def home(request):
    produto = Produtos.objects.all().order_by('descricao')
    search = request.GET.get('search') # pegar parâmetros na URL
    if search:
        produto = Produtos.objects.filter(grupo__nome__icontains=search).order_by('descricao')

    return render(request, "home.html", { 'produto': produto })

#def home(request):
#    return render(request, 'home.html')
