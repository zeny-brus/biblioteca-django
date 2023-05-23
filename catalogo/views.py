from django.shortcuts import render
from catalogo.models import Livro, LivroInstancia, Autor, Genero

def index (request):
    num_livros = Livro.objects.all().count()
    num_livro_instancias = LivroInstancia.objects.all().count()

    num_instancias_livre = LivroInstancia.objects.filter(status__exact='l').count()

    num_autor = Autor.objects.count()

    context = {
        'num_livros': num_livros,
        'num_livro_instancias': num_livro_instancias,
        'num_instancia_livre': num_instancias_livre,
        'num_autor': num_autor,
    }

    return render(request, 'index.html', context=context)
