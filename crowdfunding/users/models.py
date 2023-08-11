from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    # image = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self) -> str:
        return self.username
# Create your models here.
