from django.db import models
from django.contrib.auth.models import User
from fernet_fields import EncryptedCharField
from django.urls import reverse

# NOTE --> djfernet is the Django4+ maintained version of django-fernet-fields, and fernet_fields has to be used from that module. 


class Credential(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tag = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = EncryptedCharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_updated = models.DateTimeField(auto_now=True)
    date_last_used_successfully = models.DateTimeField(default=None, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}'s credentials for {self.tag} [{self.username}]"
    
    def get_absolute_url(self):
        return reverse("creds-detail", kwargs={"pk": self.pk})
    
    def set_password(self, password):
        self.password = password
    
