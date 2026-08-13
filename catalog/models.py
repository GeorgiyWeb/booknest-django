from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        super().save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Genres"
        

class Book(models.Model):
    
    STATUS_CHOICES = [
        ('In Stock', 'In Stock'),
        ('Out of Stock', 'Out of Stock'),
        ('Pre-order', 'Pre-order')
    ]
    
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    price_cents = models.IntegerField(default=0)
    page_count = models.IntegerField(default=0)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='In Stock')
    published_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-published_date"]
    
    def __str__(self):
        return self.title
        
        
class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        indexes = [
            models.Index(fields=['book', 'timestamp'])
        ]
    
    def __str__(self):
        return f"Order #{self.id} for {self.book.title}"
    