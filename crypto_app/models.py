from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Crypto(models.Model):
	ticker = models.CharField(max_length=10)
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	def __str__(self):
		return self.ticker
