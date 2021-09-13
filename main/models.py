from django.db import models

class Pigeons(models.Model):
    name = models.CharField(max_length= 20)
    def __str__(self):
        return self.name

class Pigeons_Info(models.Model):
    origine = models.CharField(max_length= 20)
    def __str__(self):
        return self.origine

    price = models.FloatField()


    pigeons_name = models.ForeignKey(
        'Pigeons', on_delete=models.CASCADE
    )

class Pigeons_Status(models.Model):
    status = models.BooleanField()
    def __bool__(self):
        return self.status

    Bread_name = models.ForeignKey(
        'Pigeons', on_delete=models.CASCADE
    )


