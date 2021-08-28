from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
class Livestream(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    key = models.CharField(max_length=20, unique=True)
    started_at = models.DateTimeField(null=True, blank=True)
    stopped_at = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
       return f'{self.user} : {self.key}'

    @property
    def is_live(self):
        return self.started_at is not None

    @property
    def hls_url(self):
        return reverse("hls-url", args=(self.user.username,))
