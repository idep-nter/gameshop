from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField(max_length=5)
    description = models.TextField(null=True)
    category = models.CharField(max_length=200)
    image_url = models.URLField()

    def __str__(self):
        return f"{self.title}"
