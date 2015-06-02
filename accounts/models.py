from django.contrib.auth.models import User
from django.db                  import models

class GeneralUser(models.Model):
	user = models.OneToOneField(User)
	profile_picture = models.ImageField(upload_to='user_profile//%Y/%m/%d')

	def __unicode__(self):
		return 'User: {}'.format(self.user)
