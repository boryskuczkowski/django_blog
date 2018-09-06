from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from imagefield.fields import ImageField, PPOIField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ImageField(upload_to='profile_pics',
                       auto_add_fields=True, default='default.jpg',
                       verbose_name="Profile Image",)

    def get_absolute_url(self):
        return reverse('profile')

    def __str__(self):
        return f'{self.user.username} Profile'
