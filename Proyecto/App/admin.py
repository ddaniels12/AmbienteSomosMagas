from django.contrib import admin
from .models import Producto, Schedule, Booking, Reseña

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')  # Campos a mostrar en el listado
    search_fields = ('nombre',)           # Campo de búsqueda

admin.site.register(Schedule)
admin.site.register(Booking)
admin.site.register(Reseña)