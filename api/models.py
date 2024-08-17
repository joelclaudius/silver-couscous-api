from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.name
