from django.db import models
from django.contrib.auth.models import User
from eshop_products.models import Product
from eshop_news.models import Comment


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    bought_products = models.ManyToManyField(Product)
# Create your models here.
