
19-10-> https://app.hub.la/m/uQuqcbKjxy8zfgDq2W90/p/AE9ATEyF ->filter
23-10-> https://app.hub.la/m/uQuqcbKjxy8zfgDq2W90/p/btXlUBEb ->based-views
24-10-> https://app.hub.la/m/uQuqcbKjxy8zfgDq2W90/p/ARiJPEYi ->app grupo 
25-10-> aqui https://app.hub.la/m/uQuqcbKjxy8zfgDq2W90/p/98jFSnRZ
25-10-> 2 filtros LISTVIEW 'ia passar 2 paramentros filtrados ListView para outra pagina em django'
 
https://realpython.com/django-redirects/#:~:text=Passando%20Par%C3%A2metros%20com%20Redirecionamentos,-%C3%80s%20vezes%2C%20voc%C3%AA&text=Primeiro%2C%20voc%C3%AA%20usa%20django.,o%20%C3%BAltimo%20geraria%20uma%20exce%C3%A7%C3%A3o.

python -m venv venv
venv\Scripts\activate
pip install Django
pip freeze > requirements.txt
django-admin startproject demo .
python manage.py migrate
python manage.py runserver
python manage.py startapp app


For more information on production servers see: https://docs.djangoproject.com/en/5.2/howto/deployment/

na home.html
{% block content %} 
    {% for prods in produto  %}
        <h5> {{ prods.codigo }} - {{ prods.descricao }} - {{ prods.aplicacao }} - {{ prods.grupo }} </h5> 
        
    {% endfor %}

      update na VPS
    ->sudo apt update  
    ->sudo apt install build-essential python3
    ->sudo apt install python3-dev
    ->sudo apt install python3-venv -y
    ->sudo apt install python3-pip

      COMANDOS GIT
      https://www.hostinger.com/br/tutoriais/comandos-git?utm_campaign=Generic-Tutorials-DSA|NT:Se|LO:BR-t3&utm_medium=ppc&gad_source=1&gad_campaignid=19588998604&gbraid=0AAAAADMy-haTdczLLwLupRsYSMWAKSYyJ&gclid=CjwKCAjwr8LHBhBKEiwAy47uUvUUwjeuw9Vfr5BfitORL93c_0M5mUxuNpu8K6skijTgs6z7EFRtphoCC3EQAvD_BwE#Comandos_de_branch_e_merge_do_Git

      ATUALIZAR GIT da LOCALHOST
    ->git add .   
    ->git commit -am "mensagem"
    ->git push origin main

       TRATAR CONFLITOS NA VPS
    ->git config pull.rebase true 

    ->git stash (1)
    ->git rebase --continue (2)
    
      GIT na VPS
    ->git pull

    pip install -r requirements.txt

    08-10 ki--->https://dashboard.kiwify.com/course/premium/d55ab802-47f7-40f2-a6b6-19b68ffb8e32?mod=23a557c4-1ce2-4171-b197-0357b9319b70&lesson=c1608ffd-fd2d-4001-9a52-9d55f5d671f8

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
 
comandos POSTIGRES 
->sudo -u postgres psql
->\l


04-11-25 
pip install crispy-bootstrap5
pip install django-crispy-forms
pip install django-filter
pip install crispy-bootstrap4


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
        context['grupos'] = Group.objects.filter(nome__icontains='VLR').order_by('nome')
          

        return context  