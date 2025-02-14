from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')    

    def __str__(self):
        return self.name
    

    
