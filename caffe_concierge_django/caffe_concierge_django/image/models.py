from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Image(models.Model):

    """ Image model  """
    
    name = models.CharField(max_length=50)
    caption = models.TextField()

    lat = models.CharField(max_length=30, null=True)
    lng = models.CharField(max_length=30, null=True)

    file = models.ImageField()

    def __str__(self):
        return '{}'.format(self.name)

