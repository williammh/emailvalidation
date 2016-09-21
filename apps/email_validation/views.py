from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your views here.
def index(request):
	return render(request, "email_validation/index.html")
def submit(request):
	if not EMAIL_REGEX.match(request.POST['email']):
		messages.add_message(request, messages.ERROR, 'Invalid Email!')
		return redirect('/')
	else:
		Email.objects.create(email=request.POST['email'])
	context = {
		"emails" : Email.objects.all(),
		"last" : request.POST['email']
	}
	return render(request, "email_validation/emails.html", context)
def delete(request, id):
	todelete = Email.objects.get(id=id)
	todelete.delete()
	return redirect('afterdelete')
def afterdelete(request):
	context = {
		"emails" : Email.objects.all()
	}
	return render(request, "email_validation/emails.html", context)
