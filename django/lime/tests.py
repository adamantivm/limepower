"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from lime.models import Person

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class PersonTest(TestCase):
    def test_person(self):
        tessa = Person.objects.get(pk=1)
        self.assertEqual("Tessa Lau", tessa.name)

        julian = Person.objects.get(pk=2)
        self.assertEqual("Julian Cerruti", julian.name)

        self.assertEqual(tessa.relationship, julian.relationship)
