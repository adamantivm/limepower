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
    fixtures = ['test_person.json']

    def test_person(self):
        # Test fetching known fixture People by ID
        tessa = Person.objects.get(pk=1)
        self.assertEqual("Tessa Lau", tessa.name)

        julian = Person.objects.get(pk=2)
        self.assertEqual("Julian Cerruti", julian.name)

        # Test that the relationship in these two people match
        self.assertEqual(tessa.relationship, julian.relationship)

        # Test it is possible to get from one user to the related other
        self.assertEqual(tessa, julian.loves)
        self.assertEqual(julian, tessa.loves)

    def test_gender(self):
        tessa = Person.objects.get(pk=1)
        self.assertEqual('female', tessa.gender)

        julian = Person.objects.get(pk=2)
        self.assertEqual('male', julian.gender)
