from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils import timezone


class Comment(models.Model):
    user = models.ManyToManyField(User)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.user


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    name = models.CharField(max_length=150, verbose_name='عنوان در URL')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Blog(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    authors = models.ManyToManyField(User)
    number_of_comments = models.IntegerField(default=0, null=True, blank=True)
    number_of_pingbacks = models.IntegerField(default=0, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    comments = models.ManyToManyField(Comment)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.headline


class Education(models.Model):
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    authors = models.ManyToManyField(User)
    number_of_comments = models.IntegerField(default=0, null=True, blank=True)
    number_of_pingbacks = models.IntegerField(default=0, null=True, blank=True)
    rating = models.IntegerField(default=0, null=True, blank=True)
    comments = models.ManyToManyField(Comment)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.headline