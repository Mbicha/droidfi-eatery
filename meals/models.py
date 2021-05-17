from django.db import models

# Create your models here.
class Meal(models.Model):
    combination = models.CharField(max_length=200)
    amount = models.IntegerField(default=0)
    image = models.FileField(upload_to='images/', null=True, verbose_name="")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.combination
