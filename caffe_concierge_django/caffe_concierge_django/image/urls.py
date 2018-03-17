from django.conf.urls import url
from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.ImagePredict.as_view(),
        name='list'
    ),
]
