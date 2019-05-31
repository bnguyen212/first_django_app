from first_app import views
from django.urls import re_path, path

urlpatterns = [
  re_path(r'^$', views.index, name="index"),
  path('brian/', views.brian, name="brian"),
  path('table/', views.table, name="table"),
  path('users/', views.users, name="users"),
  path('form/', views.form, name="form"),
  path('signup/', views.signup, name="signup")
]

# * necessary if using relative URL
app_name = "first_app"