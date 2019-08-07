from django.shortcuts import render, redirect
from django.views.generic.base import View
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from booksManagement.models import BookLists
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

class BookList(View, forms.Form):

	def list(request):
		objects = BookLists.objects.all()
		if request.method == "POST":
			#add user
			current_user = request.user.id
			book_list = BookLists(book_name = request.POST['book_name'],
						author = request.POST['author'],
						publication = request.POST['publication'],
						year_of_publication = request.POST['year_of_publication'],
						summary = request.POST['summary'],
						status = request.POST['status'],
						user_id = current_user)
			form = book_list.save()
			return render(request, "book_list.html", {'res':objects})
			# response = redirect('list')
			# return response
		else:
			for elt in objects:
				if elt.user_id == request.user.id:
					return render(request, "book_list.html", {'res':objects})
				else:
					response = redirect('logout')
					return response
	def book_edit(request):
		if request.method == "POST":
			objects = BookLists.objects.filter(id=request.POST['book_id'])
			return render(request, "book_edit.html", {'res':objects})
		else:
			response = redirect('logout')
			return response

	def edit(request):
		objects = BookLists.objects.all()
		# return HttpResponse('sdas')
		if request.method == "POST":
			book_list = BookLists(book_name = request.POST['book_name'],
			author = request.POST['author'],
			publication = request.POST['publication'],
			year_of_publication = request.POST['year_of_publication'],
			summary = request.POST['summary'],
			status = request.POST['status'],)
			form = book_list.save()
			# BookLists.objects.filter(id= request.POST['book_id']).update(book_list)
			return render(request, "book_list.html", {'res':objects})
