from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=50)
    prj_type = models.CharField(max_length=50,
                                choices=(('mobile', 'Mobile'), ('web', 'Web'), ('upcomming', 'Upcomming')))
    link = models.URLField()
    content = HTMLField()
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
