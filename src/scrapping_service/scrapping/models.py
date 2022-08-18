from django.db import models


# Create your models here.
from django.template.defaultfilters import slugify


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name of the location')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Name of the location'
        verbose_name_plural = 'Name of the locations'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField(max_length=50, verbose_name='Programming language')
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Programming language'
        verbose_name_plural = 'Programming languages'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Vacancies(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=250, verbose_name='Job title')
    company = models.CharField(max_length=250, verbose_name='Company')
    description = models.TextField(verbose_name='Job description')
    city = models.ForeignKey('City', on_delete=models.CASCADE, verbose_name='City')
    language = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name='Programming Language')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancies'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)