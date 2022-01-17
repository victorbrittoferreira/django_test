from django.db import models
from django.db.models import fields
#from django.db.models.fields import DecimalField, Field
#from cpf_field.models import CPFField

#from django import template


class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["id"]

    code = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=11,null=False, blank=False)
    andress = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False,blank=False, verbose_name='CPF')

    def __str__(self):
        return self.name

    def phone_mask(self):
        """
        return cellphone (00) 00000-0000 or phone(00) 0000-0000 
        """

        if self.phone and len(self.phone) >=11:
            return f'({self.phone[0:2]}){self.phone[2:7]}-{self.phone[7:11]}'

        elif self.phone:
            return f'({self.phone[0:2]}){self.phone[2:6]}-{self.phone[6:10]}'

    phone_mask.short_description = 'PHONE'  
