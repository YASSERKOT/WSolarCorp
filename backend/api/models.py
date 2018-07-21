from django.db import models

class User(models.Model):
    """This class represents the User model."""
    identifier = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    email = models.CharField(max_length=255, blank=False)
    region = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} {} {} {}".format(self.identifier, self.name, self.email, self.region)

class Layer(models.Model):
    """This class represents the Layer model."""
    identifier = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False)
    high = models.DecimalField(max_digits=19, decimal_places=2)
    width = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{} {} {} {}".format(self.identifier, self.name, self.high, self.width)