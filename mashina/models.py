from typing import Iterable
from datetime import datetime
from django.forms import ValidationError
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
    ishlab_chiqarilgan_yili = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nomi} ({self.raqam})"
    
    # def save(self, force_insert: bool = ..., force_update: bool = ..., using: str | None = ..., update_fields: Iterable[str] | None = ...) -> None:
    #     if not 1800 <= int(self.ishlab_chiqarilgan_yili) <= datetime.now().year:
    #         raise ValidationError({"detail":'Berilgan yil xato'})
    #     return super().save(force_insert, force_update, using, update_fields)
