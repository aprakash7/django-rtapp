from django.db import models

# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return str(self.id)


class Pos(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField()
