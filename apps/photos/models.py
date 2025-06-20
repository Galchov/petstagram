from django.db import models
from django.core.validators import MinLengthValidator

from apps.pets.models import Pet
from apps.photos.validators import FileSizeValidator


class Photo(models.Model):
    photo = models.ImageField(
        validators=[
            FileSizeValidator(5),
        ],
        upload_to='files',
    )
    description = models.TextField(
        max_length=300,
        validators=[
            MinLengthValidator(10),
        ],
        null=True,
        blank=True,
    )
    location = models.CharField(
        max_length=30,
        null=True,
        blank=True,
    )
    tagged_pets = models.ManyToManyField(
        to=Pet,
        blank=True,
    )
    date_of_publication = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.pk}: {self.description}"
