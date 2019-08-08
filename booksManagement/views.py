from django.shortcuts import render, redirect
from django.views.generic.base import View
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

from rest_framework import generics

from .models import BookLists
from booksManagement.models import BookLists
from .serializers import PostSerializer
from . import models
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

	def signup(request):
		if request.method == "POST":
			
			form = UserCreationForm(request.POST)

			if form.is_valid():
				form.save()
				response = redirect('/list/')
				return response
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
		response = redirect('/login/')
		return response

class BooksList(generics.ListAPIView):
    queryset = BookLists.objects.all()
    serializer_class = PostSerializer


# class BookDetail(generics.RetrieveAPIView):
#     queryset = BookLists.objects.all()
#     serializer_class = PostSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookLists.objects.all()
    serializer_class = PostSerializer

class BooksList(generics.ListCreateAPIView):
    queryset = BookLists.objects.all()
    serializer_class = PostSerializer