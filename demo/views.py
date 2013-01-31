# Create your views here.
from django.http import HttpResponse
from django.template.loader import get_template 
from django.template import Context
from datetime import datetime

def hola(request)
	return HttpResponse("hola")
