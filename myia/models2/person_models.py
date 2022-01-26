from django.db import models
from django.db.models import fields


class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["id"]

    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=15,null=False, blank=False)
    andress = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=14, null=False,blank=False, verbose_name='CPF')

    def __str__(self):
        return self.name



