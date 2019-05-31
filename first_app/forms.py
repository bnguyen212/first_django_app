from django import forms
from django.core import validators
from first_app.models import User

def start_with_z(value):
  if value[0] != 'z':
    raise forms.ValidationError('error msg')

class SignUp(forms.ModelForm):
  class Meta():
    model = User
    fields = "__all__"


class FormName(forms.Form):
  name = forms.CharField(validators=[start_with_z])
  email = forms.EmailField()
  confirm_email = forms.EmailField()
  text = forms.CharField(widget=forms.Textarea)
  # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
  #                              validators=[validators.MaxLengthValidator(0)])

  # def clean_botcatcher(self):
  #   botcatcher = self.cleaned_data['botcatcher']
  #   if len(botcatcher) > 0:
  #       raise forms.ValidationError("FOUND U A BOT")
  #   return botcatcher

  def clean(self):
    all_clean_data = super().clean()
    if all_clean_data['email'] != all_clean_data['confirm_email']:
      raise forms.ValidationError("Emails must match")