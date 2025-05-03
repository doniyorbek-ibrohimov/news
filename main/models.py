
from django.db import models
from django.db.models import Manager
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    intro = models.TextField()
    image = models.ImageField(upload_to='articles')
    author = models.CharField(max_length=100)
    read_time = models.DurationField(blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    published = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        base_slug = slugify(slug)

        count = 1
        while Article.objects.filter(slug=base_slug).exists():
            base_slug = base_slug + str(count)
            count += 1

        self.slug = base_slug

        if self.important:
            Article.objects.filter(important=True).update(important=False)

        super().save(*args, *kwargs)

    publisheds=PublishedManager()

    def __str__(self):
        return self.title


class Context(models.Model):
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='contexts/',blank=True,null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return self.text


class Comment(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()
    published = models.BooleanField(default=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True, max_length=15)
    subject = models.CharField(blank=True, null=True, max_length=255)
    message = models.TextField(blank=True, null=True)
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Newsletter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Moment(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='moments/')
    author = models.CharField(max_length=100)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
