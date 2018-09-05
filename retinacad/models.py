from django.db import models

# Create your models here.
class FundusRetina(models.Model):
    name = models.CharField(max_length=255)
    lefteye = models.FileField(upload_to='fundus/')
    righteye = models.FileField(upload_to='fundus/')
    taken_at = models.DateField(blank=False)
    uploaded_at = models.DateTimeField(auto_now_add=True)