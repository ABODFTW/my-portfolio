from django.db import models

# Create your models here.

class Object(models.Model):
	object_name = models.CharField(max_length=130)



	def __str__(self):
		return self.object_name