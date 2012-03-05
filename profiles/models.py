from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Profile(models.Model):
	user = models.ForeignKey(User)
	creation_date = models.DateTimeField( default=datetime.now)

