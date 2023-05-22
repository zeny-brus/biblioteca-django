from django.db import models
from django.urls import reverse
import uuid

class Genero(models.Model):
    name = models.CharField(max_length=200, help_text='Descreva o genero do livro')

    def __str__(self):
        return self.name

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey("Autor", on_delete=models.SET_NULL, null=True)
    sumario = models.TextField(max_length=1000, help_text='descreva uma abreviacao do livro')
    isbn = models.CharField('ISBN', max_length=13, help_text='13 Caracteres conforme <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genero = models.ManyToManyField(Genero, help_text='selecione o genero')

    def __str__(self):
        return self.titulo
    
    def get_absolute_url(self):
        return reverse('livro-detalhe', args=[str(self.id)])

class LivroInstancia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    livro = models.ForeignKey(Livro, on_delete=models.SET_NULL, null=True)
    impressao = models.CharField(max_length=200)
    retorno = models.DateField(null=True, blank=True)

    STATUS_EMPRESTIMO = (
        ('m','Manutencao'),
        ('e','Emprestado'),
        ('l','Livre'),
        ('r','Reservado'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS_EMPRESTIMO,
        blank=True,
        default='m'
    )

    class Meta:
        ordering = ['retorno']
    
    def __str__(self):
        return f'{self.id} ({self.livro.titulo})'

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField(null=True,blank=True)
    data_morte = models.DateField('Morto', null=True, blank=True)

    class Meta:
        ordering = ['sobrenome','nome']
        
    def get_absolute_url(self):
        return reverse("detalhe-autor", args=[str(self.id)])
    
    def __str__(self):
        return f'{self.sobrenome},{self.nome}'
    
    