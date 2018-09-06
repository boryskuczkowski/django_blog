import os
from django.utils.text import slugify
from django.core.files.storage import default_storage
from django.db.models import FileField


# tun this once a month in shell:
# ./manage.py cleanup_unused_media -e *.gitignore -e *.jpg -e *.JPG -e *.png -e *.jpeg --remove-empty-dirs


def unique_slug_generator(model_instance, title, slug_field):
    """
    This function will check if a slugable title exist if it does then it will add extension to make the slug unique.
    :param model_instance: which is the Model sub-class that contains our model
    :param title: This is the field we want to convert into a slugable field
    :param slug_field: this will be the name of field where want to save our slugable title to
    :return: unique slug object
    """
    slug = slugify(title)
    model_class = model_instance.__class__

    while model_class._default_manager.filter(slug=slug).exists():

        object_pk = model_class._default_manager.latest('pk')
        object_pk = object_pk.pk + 1

        slug = f'{slug}-{object_pk}'

    return slug
