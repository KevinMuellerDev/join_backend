from django.db import models

# Create your models here.
class Tasks(models.Model):
    category = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.category


class Summary(models.Model):
    pass


class Contacts(models.Model):
    pass
