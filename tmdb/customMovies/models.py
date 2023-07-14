from django.db import models


# Create your models here.
class Movie(models.Model):
    tittle = models.CharField(max_length=200, verbose_name="Título")
    overview = models.TextField(blank=True, verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen", upload_to='movies')
    rate = models.FloatField(null=True, verbose_name="Valoración media")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle

    class Meta:
        verbose_name = "pelicula"
        verbose_name_plural = "peliculas"
        ordering = ['-created']
