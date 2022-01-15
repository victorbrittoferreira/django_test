from django.db import models
from django.db.models import fields
from django.db.models.fields import DecimalField, Field


class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["id"]

    code = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=11, null=False, blank=False)
    andress = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False,blank=False, verbose_name='CPF')

    def __str__(self):
        return self.name
