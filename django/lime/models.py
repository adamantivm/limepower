from django.db import models

# Create your models here.

class Relationship(models.Model):
    """A connection between two (or more) people"""
    pass

class Person(models.Model):
    """Half of a relationship"""
    name = models.CharField(max_length=256, blank=False)
    email = models.CharField(max_length=256, blank=False)
    relationship = models.ForeignKey(Relationship)
