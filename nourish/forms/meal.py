from django import forms
from nourish.models import EventUser, Event, GroupUser, Group, EventGroup, Meal, MealInvite
from django.forms.extras.widgets import SelectDateWidget
from django.contrib.auth.models import User
from django.core.validators import ValidationError
from django.forms import ModelForm

class EventGroupInviteForm(forms.Form):
    meals = forms.ModelMultipleChoiceField(queryset=Meal.objects.all(),widget=forms.CheckboxSelectMultiple)

class EventGroupMealForm(forms.Form):
    meal_id = forms.IntegerField(widget=forms.HiddenInput)
    date = forms.CharField(widget=forms.HiddenInput, required=False)
    members = forms.IntegerField(widget=forms.TextInput(attrs={'size':'3'}))
    invite = forms.ChoiceField(choices=[], widget=forms.RadioSelect)

class EventGroupInvitesForm(forms.Form):
    invite_id = forms.IntegerField(widget=forms.HiddenInput)
    action = forms.BooleanField(required=False)

class MealForm(ModelForm):
    class Meta:
        model = Meal

class MealStubForm(forms.Form):
    date = forms.DateField(widget=forms.HiddenInput, required=False)
    members = forms.IntegerField(widget=forms.TextInput(attrs={'size':3}), required=False)
    features = forms.ChoiceField(choices=( ('', 'No'), ('R', 'Yes')), required = False)
    notes = forms.CharField(required=False)
