from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class MyUserManager(BaseUserManager):
    def create_user(self, email, name, gender, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=MyUserManager.normalize_email(email),
            name=name,
            gender=gender
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, gender, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            name=name,
            gender=gender,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Relationship(models.Model):
    """A connection between two (or more) people"""
    pass

class Person(AbstractBaseUser):
    """Half of a relationship"""
    email = models.CharField(max_length=256, blank=False,
        verbose_name='email address', unique=True, db_index=True)
    name = models.CharField(max_length=256, blank=False)
    
    # We assume that each person is in at most one relationship
    # We assume (though do not enforce) that a relationship contains only
    # two people
    relationship = models.ForeignKey(Relationship, blank=True, null=True)

    # Nickname for the other person in the relationship
    nickname = models.CharField(max_length=256, blank=False)

    # This person's online status
    status = models.BooleanField()
    last_updated = models.DateTimeField(auto_now=True)

    # Gender, "male" or "female"
    gender = models.CharField(max_length=10, blank=False)

    # Calculated field: which other user is this user
    # connected to?
    def get_related_person(self):
        res = Person.objects.filter(relationship=self.relationship).exclude(id=self.id)
        return res[0]

    loves = property(get_related_person)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','gender']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

