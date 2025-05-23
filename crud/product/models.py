from django.db import models
from categories.models import Category, Tag

class Product(models.Model):
    name = models.CharField(max_length=255)  # Short text
    description = models.TextField()  # Long text
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Fixed-precision decimal
    stock = models.IntegerField()  # Numeric value
    available = models.BooleanField(default=True)  # Boolean
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp with updates
    image = models.ImageField(upload_to='products/')  # Image upload
    data = models.JSONField(null=True, blank=True)  # JSON storage
    
    category = models.ForeignKey( Category , on_delete=models.CASCADE)  # Many-to-One
    tags = models.ManyToManyField(Tag)  # Many-to-Many
    
    def __str__(self):
        return self.name  # String representation

