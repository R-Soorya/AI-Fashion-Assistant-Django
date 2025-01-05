from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Outfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outfits')
    name = models.CharField(max_length=100)
    image = models.ImageField( upload_to='outfits/')
    color = models.CharField(max_length=100)
    category = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} ({self.category})"
    

class OutfitPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='outfit_plans')
    date = models.DateField()
    top = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='top_plans')
    bottom = models.ForeignKey(Outfit, on_delete=models.CASCADE, related_name='bottom_plans')
    color = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plan genreated for {self.user.username}"

    