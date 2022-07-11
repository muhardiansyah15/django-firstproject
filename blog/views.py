from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	context = {
        'title' : 'On the rainbow connection number of triangle-net graph',
        'contributor' : 'Muhardiansyah',
    }
	return render(request, 'blog/index.html', context)
