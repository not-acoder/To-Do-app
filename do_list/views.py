from django.shortcuts import render , redirect
from .models import List
from .forms import ListForm
from django.contrib import messages 
from django.http import HttpResponseRedirect
def home(request):
	if request.method == "POST":
		form = ListForm(request.POST or None)
		if form.is_valid():
			form.save()
			all_items = List.objects.all
			messages.success(request ,("Gear up! Task added!!"))
			return render(request , 'home.html' ,{'all_items' : all_items})

	else:
		all_items = List.objects.all
		return render(request , 'home.html' ,{'all_items' : all_items})
def about(request):
	context = {}
	return render(request , 'about.html' ,context)

def delete(request,list_id):
	item = List.objects.get(pk=list_id)
	item.delete()
	messages.success(request ,("Wohoo Task Finished!!"))
	return redirect('home')

def status(request , list_id):
	item = List.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def unstatus(request , list_id):
	item = List.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')