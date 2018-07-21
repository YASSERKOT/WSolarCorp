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