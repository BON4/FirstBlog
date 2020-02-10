from django.shortcuts import render
from .models import Post
from django.views import View
from django.core.serializers import serialize
from django.http import JsonResponse
import json

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


class PostListView(View):
    def get(self, request):
        context = []
        for item in Post.objects.all():
            context.append((item.as_dict()))

        return JsonResponse(context, safe=False)

# Create your views here.
