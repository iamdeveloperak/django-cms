from django.db import models
from cms.models import CMSPlugin


class FeatureServiceCardPluginModel(CMSPlugin):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.title


class SocialIconsPluginModel(CMSPlugin):
    name = models.CharField(max_length=100)
    link = models.URLField()
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.link