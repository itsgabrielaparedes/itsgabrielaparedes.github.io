from django.contrib import admin
from .models import Producto
from django.utils.safestring import mark_safe

# Register your models here.
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'nombre', 'descripcion', 'ingrediente', 'tipo_de_piel', 'problemas_piel', 'display_foto')

    def display_foto(self, obj):
        return mark_safe('<img src="{}" width="50" height="50" />'.format(obj.foto.url))

    display_foto.short_description = 'Foto'

admin.site.register(Producto, ProductoAdmin)