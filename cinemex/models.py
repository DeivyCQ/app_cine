from django.db import models

# Create your models here.

# Cinema Model.
class Cinema(models.Model):
    cinema_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Cine'
        verbose_name_plural = 'Cines'