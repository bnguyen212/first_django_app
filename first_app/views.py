from django.shortcuts import render, redirect
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord, User
from . import forms

# Create your views here.
def index(request):
  # my_dict = {'insert_me': "Hello I am from views.py"}
  return render(request, 'first_app/index.html')
  # return HttpResponse("<em>Helo Brian!</em>")


def brian(request):
  return HttpResponse("<strong>I miss you</strong>")

def signup(request):
  form = forms.SignUp()
  if request.method == "POST":
    form = forms.SignUp(request.POST)
    if form.is_valid():
      form.save(commit=True)
      return users(request)
  return render(request, 'first_app/form.html', context={'form':form})


def table(request):
  webpages_list = AccessRecord.objects.order_by('date')
  date_dict = {'access_records' : webpages_list }
  return render(request, 'first_app/table.html', context=date_dict)

def form(request):
  form = forms.FormName();
  if request.method == "POST":
    form = forms.FormName(request.POST)
    if form.is_valid():
      print("validation success")
      print(form.cleaned_data['name'])
      print(form.cleaned_data['email'])
      print(form.cleaned_data['text'])

  return render(request, 'first_app/form.html', {'form':form})

def users(request):
  users_list = User.objects.order_by('last_name')
  user_dict = {'users': users_list}
  return render(request, 'first_app/users.html', context=user_dict)
