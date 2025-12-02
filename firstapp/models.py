from django.db import models

# Create your models here.
class Fruit(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=255)
    price=models.FloatField()
    color=models.CharField(max_length=100)
    updated_at=models.DateField(auto_now=True)
    created_at=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name