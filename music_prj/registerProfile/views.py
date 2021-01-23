from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect


class NameForm(forms.Form):
    yourName = forms.CharField(label="Your name", max_length=100, widget=forms.Textarea)


def index(request):
    context = { 'current_name': '임시이름' }
    return render(request, 'registerProfile/index.html', context)