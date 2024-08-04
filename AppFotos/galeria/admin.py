from django.contrib import admin

from galeria.models import Foto, Nota, Tarea

# Register your models here.

class NotaInline(admin.StackedInline):  # Puedes usar admin.TabularInline para una vista más compacta
    model = Nota
    extra = 0  # Cuántos formularios en línea mostrar inicialmente

class TareaAdmin(admin.ModelAdmin):
    inlines = [NotaInline]
    list_display = ['nombre']

admin.site.register(Tarea, TareaAdmin)


class FotosAdmin(admin.ModelAdmin):
    list_display = ['imagen']
admin.site.register(Foto, FotosAdmin)