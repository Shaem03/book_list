from django.shortcuts import render, redirect
from django.views.generic.base import View
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
# from django.template import Template, Context
# from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext
# from passlib.hash import pbkdf2_sha256
# from django.core.mail import send_mail, BadHeaderError
# import smtplib
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib import messages

class HomePage(View, forms.Form):

	def home(request):
		today = datetime.datetime.now().date()
		name = "muhammed shaheem"
		daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
		data = {
			"todays_data" : today,
			"name" : name,
			"daysOfWeek" : daysOfWeek
		}
		return render(request, "home.html", {"data" : data})

	def signup(request):
		if request.method == "POST":
			
			form = UserCreationForm(request.POST)

			if form.is_valid():
				form.save()
				return render(request, "index.html")
		else:
			form = UserCreationForm()

		return render(request, "signup_form.html", {'form':form})

	def login(request):
		if request.method == "POST":
			form = AuthenticationForm(data=request.POST)
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				response = redirect('/list/')
				return response
		else:
			form = AuthenticationForm()
		return render(request, "login_form.html", {'form':form})

	def logout(request):
		logout(request)
		# return render(request, "login_form.html")
		response = redirect('/login/')
		return response
