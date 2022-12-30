from django.db import models
from django.contrib.auth.models import User
import uuid

weight_choices = (
    ('kg', 'kg'),
    ('lbs', 'lbs'),
)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=400)
    username = models.CharField(max_length=50)
    location = models.CharField(max_length=200, blank=True, null=True)
    metric = models.CharField(choices=weight_choices,
                              max_length=3, default='kg')
    weight = models.DecimalField(
        max_digits=7, decimal_places=2, blank=True, null=True)
    calorie_goal = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)


class WeightLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=7, decimal_places=2)
    entry_date = models.DateField()
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        ordering = ['-entry_date']

    def __str__(self):
        return f"{self.user.username} - {self.weight} kg on {self.entry_date}"
