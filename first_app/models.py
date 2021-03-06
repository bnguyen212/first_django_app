from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)

  portfolio_site = models.URLField(blank="True")
  profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

  def __str__(self):
      return self.user.username


# Create your models here.
# class User(models.Model):
#   first_name = models.CharField(max_length=50);
#   last_name = models.CharField(max_length=50);
#   email = models.EmailField(max_length=128, unique=True);

#   def __str__(self):
#     return "{}, {} ({})".format(self.last_name, self.first_name, self.email)

class Topic(models.Model):
  top_name = models.CharField(max_length=264, unique=True)

  def __str__(self):
    return self.top_name

class Webpage(models.Model):
  topic = models.ForeignKey(Topic, on_delete=models.DO_NOTHING)
  name = models.CharField(max_length=264, unique=True)
  url = models.URLField(unique=True)

  def __str__(self):
    return self.url

class AccessRecord(models.Model):
  name = models.ForeignKey(Webpage, on_delete=models.DO_NOTHING)
  date = models.DateField()

  def __str__(self):
    return str(self.date)
