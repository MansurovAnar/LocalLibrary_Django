from django.shortcuts import render
from django.http import HttpResponse

# Create your views here
def index(request):
	return HttpResponse("<html><head><title>LocalTest</title></head>"
		+ "<body>Tested</body></html>")

