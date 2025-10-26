from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.HomeListView.as_view(), name="home"),
    path('volare/', views.VolareListView.as_view(), name="volare"),
    #path('volare/', views.VolareLisView.as_view(), name="volare"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

