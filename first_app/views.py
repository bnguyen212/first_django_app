from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from first_app.models import Topic, Webpage, AccessRecord #User
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
  # my_dict = {'insert_me': "Hello I am from views.py"}
  context_dict = {"text": 'hello my Name iS bRiaN', "num": 500}
  return render(request, 'first_app/index.html', context_dict)
  # return HttpResponse("<em>Helo Brian!</em>")

@login_required #only accessible if logged in
def user_logout(request):
  logout(request)
  return HttpResponseRedirect(reverse('first_app:index'))

def user_login(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    user = authenticate(username=username, password=password)

    if user:
      if user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('first_app:index'))
      else:
        return HttpResponse("Account not active")
    else:
      print('Someone failed to login')
      return HttpResponse('invalid credentials')
  else:
    return render(request, 'first_app/login.html', {})

def register(request):
  registered = False
  if request.method == "POST":
    user_form = forms.UserForm(data=request.POST)
    profile_form = forms.UserProfileInfoForm(data=request.POST)
    if user_form.is_valid() and profile_form.is_valid():
      user = user_form.save()
      user.set_password(user.password)
      user.save()

      profile = profile_form.save(commit=False)
      profile.user = user

      if 'profile_pic' in request.FILES:
        profile.profile_pic = request.FILES['profile_pic']

      profile.save()

      registered = True
    else:
      print(user_form.errors, profile_form.errors)
  else:
    user_form = forms.UserForm()
    profile_form = forms.UserProfileInfoForm()

  return render(request, 'first_app/registration.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

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

# def users(request):
#   users_list = User.objects.order_by('last_name')
#   user_dict = {'users': users_list}
#   return render(request, 'first_app/users.html', context=user_dict)
