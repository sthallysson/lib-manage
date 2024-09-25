from django.db import models

# Create your models here.


class Book_type(models.Model):
    type = models.CharField(max_length=200)

    def __str__(self):
        return self.type


class Genre(models.Model):
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.genre

# Collection - tabela que armazena os livros


class Collection(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')
    author = models.CharField(max_length=200, verbose_name='Autor')
    year = models.IntegerField(blank=True, verbose_name='Ano de lançamento')
    isbn = models.CharField(max_length=20, blank=True, verbose_name='ISBN')
    picture = models.ImageField(
        upload_to='book_pictures/%Y/%m', verbose_name='Imagem', blank=True)
    book_count = models.IntegerField(verbose_name='Livros em Estoque')
    description = models.TextField(blank=True, verbose_name='Descrição')
    type = models.ForeignKey(
        # type - tipo do material (livro, revista, jornal, etc)
        Book_type, on_delete=models.SET_NULL, null=True, verbose_name='Tipo')
    # genre - genero do livro
    # tem que salvar uma lista de generos
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Gênero')

    def __str__(self):
        return self.title
