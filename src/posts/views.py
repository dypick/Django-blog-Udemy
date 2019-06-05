from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post

def post_create(request):
	context_data = {
		"title":"create"
	}
	return render(request, "index.html", context_data)

def post_detail(request): #retieve
	context_data = {
		"title":"Detail"
	}
	return render(request, "index.html", context_data)

def post_list(request):
	queryset = Post.objects.all()
	# if request.user.is_authenticated():
	context_data = {
		"object_list": queryset,
		"title":" UserList"

	}
	# else:
	# 	context_data = {
	# 	"title":"List"

	# }
	return render(request, "index.html", context_data)

def post_update(request):
	context_data = {
		"title":"Update"

	}
	return render(request, "index.html", context_data)

def post_delete(request):
	context_data = {
		"title":"Delete"

	}
	return render(request, "index.html", context_data)


