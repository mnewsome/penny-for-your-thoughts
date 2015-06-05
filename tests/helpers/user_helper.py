from django.contrib.auth.models import User

from accounts.models import GeneralUser

def create_user(username='TBone', email='some@email.com', password='password'):
  return User.objects.create(username=username, email=email)

def create_general_user(username='GeneralTBone', email='some@email.com', password='password'):
  user = User.objects.create(username=username, email=email)
  GeneralUser.objects.create(user=user)
  return  user