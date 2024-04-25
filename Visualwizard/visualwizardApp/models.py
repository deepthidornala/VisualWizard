from django.db import models

# Create your models here.

class EnhancedImage(models.Model):
    original_image = models.ImageField(upload_to='originals/')
    enhanced_image = models.ImageField(upload_to='enhanced/', blank=True)  # Optional for storing enhanced image
    timestamp = models.DateTimeField(auto_now_add=True)  # Record upload time
