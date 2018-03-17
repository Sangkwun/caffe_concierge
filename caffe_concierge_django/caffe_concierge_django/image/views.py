from django.shortcuts import render

from .cnn_model.image_predict import image_to_caffe
from django.core.files.uploadedfile import InMemoryUploadedFile, SimpleUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

from PIL import Image
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models
import json


class ImagePredict(APIView):
    def post(self, request, format=None):
 
        print(request.data)
        image = request.FILES["image"]

        result = image_to_caffe(image)

        caffe = models.Image.objects.get(name=result)
        serializer = serializers.ImageSerializer(caffe)


        return Response(data=serializer.data, status=status.HTTP_200_OK)
        # return Response(data="hello", status=status.HTTP_200_OK)
