from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Dune.Status.PUBLISHED)


class Dune(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)  # Необязательное поле - blank
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.DRAFT)
    cat = models.ForeignKey(to='Category', on_delete=models.PROTECT, related_name='posts')   # post - менеджер
    tags = models.ManyToManyField(to='TagPost', blank=True, related_name='tags')
    planet = models.ForeignKey(to='Planet', on_delete=models.PROTECT, null=True,
                                  blank=True, related_name='characters')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Персонажи дюны'
        verbose_name_plural = 'Персонажи дюны'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    year = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Planet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    count_satellites = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

