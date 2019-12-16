from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	phone = models.CharField(max_length=11)
	address = models.CharField(max_length=255)
	town = models.CharField(max_length=45)
	post_code = models.CharField(max_length=45)
	country = models.CharField(max_length=45)

	class Meta:
		verbose_name_plural = 'User Details'

	def __str__(self):
		user = User.objects.get(id=self.user.pk)
		return str(self.user) + " " + str(user.last_name)
