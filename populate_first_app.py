import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sample.settings')

import django
django.setup()

import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
  t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
  t.save()
  return t

def populate(N=5):
  for entry in range(N):
    top = add_topic();
    fake_url = fakegen.url()
    fake_date = fakegen.date()
    fake_name = fakegen.company()
    wb = Webpage.objects.get_or_create(topic=top, url=fake_url,name=fake_name)[0]
    acc_rec = AccessRecord.objects.get_or_create(name=wb, date=fake_date)[0]

def make_users(N=20):
  for num in range(N):
    fake_name = fakegen.name().split()
    first_name = fake_name[0]
    last_name = fake_name[1]
    fake_email = fakegen.email()
    User.objects.get_or_create(first_name=first_name, last_name=last_name, email=fake_email)

if __name__ == '__main__':
  print('populating script')
  # populate(20)
  make_users(50)
  print('complete')