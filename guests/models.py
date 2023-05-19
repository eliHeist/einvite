from django.db import models

# Create your models here.
class Guest(models.Model):
   name = models.CharField(max_length=50)
   phone = models.CharField(max_length=50, unique=True)
   email = models.EmailField(blank=True, null=True)
   is_active = models.BooleanField(default=True)

   def __str__(self):
      return self.name