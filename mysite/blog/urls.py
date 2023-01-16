from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.post_list, name='post_list'),
    path('acercade/',views.acercade, name='acercade'),
    path('contacto/', views.contacto, name='contacto'),

]