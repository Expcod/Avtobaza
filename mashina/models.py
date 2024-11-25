from django.db import models

class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    familiya = models.CharField(max_length=50)
    jshshir = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return f"{self.ism} {self.familiya} ({self.jshshir})"


class Mashina(models.Model):
    haydovchi = models.ForeignKey(Haydovchi, on_delete=models.CASCADE, related_name='mashinalar')
    raqam = models.CharField(max_length=15, unique=True)
    nomi = models.CharField(max_length=50)
    rangi = models.CharField(max_length=30)
    ishlab_chiqarilgan_yili = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nomi} ({self.raqam})"
