from django.db import models
from django.db.models import fields

from django import forms



class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["id"]

    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=11,null=False, blank=False)
    andress = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False,blank=False, verbose_name='CPF')

    def __str__(self):
        return self.name

    #def __init__(self,*args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['phone'].widget.attrs.update({'class': 'mask-phone'})
    #    self.fields['cpf'].widget.attrs.update({'class': 'mask-cpf'})



