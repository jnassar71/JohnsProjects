from django.db import models
from django.db.models import CharField
from django.db.models import DateField
from django.db.models import IntegerField

class Location(models.Model):
    LocationName = CharField(max_length=100)

    def __str__(self):
        return self.LocationName

class Person(models.Model):
    FirstName = CharField(max_length=100)
    LastName = CharField(max_length=100)
    Address = CharField(max_length=500)
    City = CharField(max_length=100)
    State = CharField(max_length=100)
    Zip = CharField(max_length=20)

    def __str__(self):
        return self.FirstName + ' ' + self.LastName


class Case(models.Model):
    CaseName = CharField(max_length=100)
    CaseDate = DateField(auto_now=True)

    def __str__(self):
        return self.CaseName

class Contract(models.Model):
    ContractNumber = IntegerField(primary_key=True)
    DateCreated = DateField(auto_now=True)

    def __str__(self):
        return str(self.ContractNumber)

class ContractDetails(models.Model):
    Description = CharField(max_length=100)
    ContractID = models.ForeignKey(Contract, default=1, verbose_name="Contract", on_delete=models.SET_DEFAULT)

    class Meta:
        verbose_name_plural = "ContractDetails"

    def __str__(self):
        return self.Description