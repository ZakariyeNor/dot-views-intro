from django.db import models

# Create your models here.
# oauth/models.py
from oauth2_provider.models import AbstractApplication

class MyApplication(AbstractApplication):
    post_logout_redirect_uris = models.TextField(blank=True, default="")
