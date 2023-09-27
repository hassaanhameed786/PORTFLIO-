from typing import Any
from django.db import models


# Database are like in the Django (ORM)
class  Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=100)


