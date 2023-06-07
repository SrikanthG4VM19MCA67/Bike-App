from django.db import models

# Create your models here.
class Bike(models.Model):
    company=models.CharField(max_length=30)
    picture=models.ImageField()
    modelname=models.CharField(max_length=20)
    cc=models.IntegerField()
    price=models.BigIntegerField()

    def __str__(self):
        return self.modelname