from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now
from datetime import timedelta


class Organization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class OrganizationMembership(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='members')

    def __str__(self):
        return f"{self.user} {self.organization}"

class Kudos(models.Model):
    giver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="given_kudos")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_kudos")
    message = models.TextField(max_length=280, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(giver=models.F("receiver")), name="prevent_self_kudos")
        ]

    def __str__(self):
        return f"{self.giver} → {self.receiver} ({self.timestamp.date()})"
