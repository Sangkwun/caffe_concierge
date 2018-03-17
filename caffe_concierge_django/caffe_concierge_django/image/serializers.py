from rest_framework import serializers
from . import models


class ImageSerializer(serializers.ModelSerializer):
    """ Used for notifications """
    class Meta:
        model = models.Image
        fields = (
            'name',
            'caption',
            'file'
        )