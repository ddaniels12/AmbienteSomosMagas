from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página de inicio
    path('productos/', views.productos, name='productos'),  # Página de productos
    path('servicios/', views.servicios, name='servicios'),  # Página de servicios
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
    path('schedule_list/', views.schedule_list, name='schedule_list'),
    path('schedule_page/', views.schedule_page, name='schedule_page'),
    path('book_schedule/<int:schedule_id>/', views.book_schedule, name='book_schedule'),
    path('anadir_al_carro/<int:id>/', views.anadir_al_carro, name='anadir_al_carro'),
    path('reducir_del_carro/<int:id>/', views.reducir_del_carro, name='reducir_del_carro'),
    path('aumentar_del_carro/<int:id>/', views.aumentar_del_carro, name='aumentar_del_carro'),
    path('eliminar_del_carro/<int:id>/', views.eliminar_del_carro, name='eliminar_del_carro'),
    path('get-cart-data/', views.get_cart_data, name='get_cart_data'),
]
