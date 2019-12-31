import datetime
from django.http import HttpResponse, Http404

def hello(request):
	return HttpResponse("Hello World")

def current_datetime(request):
	now = datetime.datetime.now()
	html = "It is now %s." % now
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except TypeError:
		raise Http404
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "In %s hours(s).It will be %s." % (offset, dt)
	return HttpResponse(html)
