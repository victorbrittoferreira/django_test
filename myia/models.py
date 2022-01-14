from django.db import models

class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["id"]

    code = models.CharField(max_length=255, null=False, blank=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=11, null=False, blank=False)
    andress = models.CharField(max_length=255, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    
 

    def __str__(self):
        return "#{}".format(self.code)

