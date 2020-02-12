from django.shortcuts import render
from .models import Post
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


@method_decorator(csrf_exempt, name='dispatch')
class PostListView(View):
    def get(self, request):
        context = []
        for item in Post.objects.all():
            context.append((item.as_dict()))

        return JsonResponse(context, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class PostLikeView(View):
    def post(self, request, pk):
        err = ''
        if request.method == 'POST':
            p = Post.objects.get(id=pk)
            err = p.like_post(request.POST['user_id'])
        return JsonResponse({'err': err})


@method_decorator(csrf_exempt, name='dispatch')
class PostDisLikeView(View):
    def post(self, request, pk):
        err = ''
        if request.method == 'POST':
            p = Post.objects.get(id=pk)
            err = p.dislike_post(request.POST['user_id'])
        return JsonResponse({'err': err})
# Create your views here.
