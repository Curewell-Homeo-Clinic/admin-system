from django.shortcuts import redirect


# redirect index to admin panel
def index(request):
	response = redirect('/admin/')
	return response
