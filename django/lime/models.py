from django.db import models

# Create your models here.

class Relationship(models.Model):
    """A connection between two (or more) people"""
    pass

class Person(models.Model):
    """Half of a relationship"""
    name = models.CharField(max_length=256, blank=False)
    email = models.CharField(max_length=256, blank=False)
    
    # We assume that each person is in at most one relationship
    # We assume (though do not enforce) that a relationship contains only
    # two people
    relationship = models.ForeignKey(Relationship)

    # Nickname for the other person in the relationship
    nickname = models.CharField(max_length=256, blank=False)

    # This person's online status
    status = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True)

    # Calculated field: which other user is this user
    # connected to?
    def get_related_person(self):
        res = Person.objects.filter(relationship=self.relationship).exclude(id=self.id)
        return res[0]

    loves = property(get_related_person)
