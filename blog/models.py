import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from imagefield.fields import ImageField, PPOIField
from category.models import Category


class Post(models.Model):
  title = models.CharField(max_length=100)
  content = models.TextField()
  slug = models.SlugField(max_length=100, blank=True)
  date_posted = models.DateTimeField(default=timezone.now)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  comments = GenericRelation(Comment)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
  image = ImageField(upload_to='post_pics',
                     auto_add_fields=True, blank=True,
                     verbose_name="Main Image / Thumbnail",)

  def __str__(self):
    return self.title

  def get_absolute_url(self):

    return reverse('post-detail', kwargs={'pk': self.pk})


def slug_save(sender, instance, *args, **kwargs):

  if not instance.slug:
    instance.slug = unique_slug_generator(instance, instance.title, instance.slug)


pre_save.connect(slug_save, sender=Post)
