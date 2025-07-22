from django.db import models
from django.core.validators import MinValueValidator

class Book(models.Model):
    
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField(validators=[MinValueValidator(1)])
    image_url = models.CharField(max_length=255)

    def __str__(self):
        return self.title 