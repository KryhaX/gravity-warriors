from django.db import models
from django.db.models import Model

class Dips(models.Model):

    username = models.CharField(max_length=64 , blank=False ,unique=True)
    weight = models.DecimalField(max_digits=3, decimal_places=1,
                                      null=True, blank=True)
    date = models.DateField(blank=True, null=True)

    rank = models.PositiveIntegerField(blank=False, default=0)


    def Dips_display(self):
        return "{}st - {} - ({})kg".format(self.rank, self.username, self.weight)


    def __str__(self):
        return self.Dips_display()

class Pull_ups(models.Model):

    username = models.CharField(max_length=64, blank=False, unique=True)
    weight = models.DecimalField(max_digits=3, decimal_places=1,
                      null=True, blank=True)
    date = models.DateField(blank=True, null=True)

    rank = models.PositiveIntegerField(null=False, blank=False , default=0)


    def Pull_ups_display(self):
        return "{}st - {} - ({})kg".format(self.rank, self.username, self.weight)

    def __str__(self):
        return self.Pull_ups_display()