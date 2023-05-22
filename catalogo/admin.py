from django.contrib import admin
from catalogo.models import Autor, Livro, Genero, LivroInstancia



admin.site.register(Genero)

class LivroInstanciaInLine(admin.TabularInline):
    model = LivroInstancia

class LivroInLine(admin.TabularInline):
    model = Livro

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('sobrenome','nome','data_nascimento','data_morte')
    fields = ['nome','sobrenome',('data_nascimento', 'data_morte')]
    inlines = [LivroInLine]

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo','autor','display_genero')
    inlines = [LivroInstanciaInLine]


@admin.register(LivroInstancia)
class InstanciaAdmin(admin.ModelAdmin):
    list_display = ('livro','id','status','retorno')
    list_filter = ('status','retorno')
    fieldsets = (
        (None, {
            'fields': ('livro', 'impressao', 'id')
        }),
        ('Avaliação', {
            'fields': ('status', 'retorno')
        }),
    )