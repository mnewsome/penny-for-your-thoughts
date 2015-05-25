from django.contrib.auth.models import User

def create_user(username='TBone', email='some@email.com', password='password'):
  return User.objects.create(username=username, email=email)
