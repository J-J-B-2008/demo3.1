
14-10-> https://app.hub.la/m/uQuqcbKjxy8zfgDq2W90/p/3aU2zMpk

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

      atualizar GIT da LOCALHOST
    ->git add .   
    ->git commit -am "mensagem"
    ->git push origin main

       tratar erros na vps
    ->git config pull.rebase true   

      GIT na VPS
    ->git pull

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
