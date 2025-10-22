from django.shortcuts import render
from app.models import Produtos

def home(request):
    produto = Produtos.objects.all().order_by('descricao')
    search = request.GET.get('search') # pegar parâmetros na URL
    if search:
        produto = Produtos.objects.filter(grupo__nome__icontains=search).order_by('descricao')

    return render(request, "home.html", { 'produto': produto })

def volare(request):   
       
    volareproduto = Produtos.objects.filter(montadora__nome__icontains='volare').order_by('descricao')
    search =  request.GET.get('search')
    if search:
        volareproduto = Produtos.objects.filter(aplicacao__icontains=search).order_by('descricao')

    context = {
        'volareproduto' : volareproduto,
        'search' : search

    }
    return render(request, 'volare.html', context)

    