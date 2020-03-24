from django.http import HttpResponse
from django.shortcuts import render

from First_app.models import BlogPost


def index(request):
    posts = BlogPost.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)
