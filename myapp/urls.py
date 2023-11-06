from django.urls import path
#from . import views
from . import views


urlpatterns = [
    path('', views.registro_iniciar_sesion, name='registro_iniciar_sesion'),
    path('website/', views.productos),
    path('form_rec/', views.form_rec, name='form_rec'),
    path('prod_rec/', views.productos_recomendados,name='productos_recomendados')
]