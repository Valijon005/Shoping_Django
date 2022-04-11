from django.urls import path
from .import views

urlpatterns = [
    path('', views.stor, name='main'),
    path('card/', views.card, name='card'),
    path('checout/',views.checout, name='checout'),
    path('stor/',views.stor, name='stor'),
    path('update_item/',views.updeteitm, name='updateitem'),
    # path('tushganpul/',views.kelganpul, name='kelganpul'),
    # path('shop/',views.shop, name='shop'),
]
