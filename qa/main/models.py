from django.db import models
from django.contrib.auth.models import User
from userena.models import UserenaBaseProfile

class UserProfile(UserenaBaseProfile):
    '''
    This is django user profile .
    '''
    user = models.OneToOneField(User, unique=True)
    last_login = models.DateTimeField(auto_now_add = True)
    question = models.CharField(max_length=100, blank=True)
    answer = models.CharField(max_length=100, blank=True)

