from django.contrib import admin
from .models import Almuerzo, Desayuno, Ensalada, Crema

# Register your models here.
class EnsaladaAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')

admin.site.register(Ensalada, EnsaladaAdmin)

class CremaAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')

admin.site.register(Crema, CremaAdmin)

class DesayunoAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')

admin.site.register(Desayuno, DesayunoAdmin)

class AlmuerzoAdmin(admin.ModelAdmin):
    list_display = ('name', 'priceM', 'priceL')

admin.site.register(Almuerzo, AlmuerzoAdmin)