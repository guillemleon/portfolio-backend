from django.db import models
from cloudinary.models import CloudinaryField
from cloudinary.uploader import destroy

class ProjectQuerySet(models.QuerySet):
    def delete(self, *args, **kwargs):
        for obj in list(self):
            obj.delete(*args, **kwargs)
        super().delete(*args, **kwargs)


class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    start_date  = models.DateField(null=True, blank=True)
    end_date    = models.DateField(null=True, blank=True)
    url         = models.URLField(null=True, blank=True)
    image       = CloudinaryField('image', null=True, blank=True)

    objects = ProjectQuerySet.as_manager()

    def delete(self, *args, **kwargs):
        if self.image and getattr(self.image, 'public_id', None):
            destroy(self.image.public_id)
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
