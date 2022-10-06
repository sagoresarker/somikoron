from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER = (
    (0, 'Male'),
    (1, 'Female'),
    (2, 'Prefer Not to Say')
)

class CustomUser(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    gender = models.IntegerField(choices=GENDER, default=2)
    phone = models.IntegerField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.username


