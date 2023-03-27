""" """
from django.db import models
from django.core.validators import FileExtensionValidator


class Category(models.Model):
    """
    Category model to represent different product categories.
    Examples include Computers, Servers, and Mobile Devices.
    """

    name = models.CharField(max_length=32, primary_key=True, editable=True)
    description = models.TextField()
    image = models.ImageField(
        upload_to="categories/",  # !TODO change to /var/TuxTech/media
        validators=[
            FileExtensionValidator(
                allowed_extensions=["png", "svg"],
                message="File format not supported.",
            )
        ],
        null=False,
    )

    def __str__(self):
        """ """
        return self.name
