from django.shortcuts import render, redirect
from django.http import Http404
from .forms import UserRegisterForm
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from users.models import User

def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404('User does not exist or is already verified')

    user.is_verified = True
    user.save()
    messages.success(request, f"Your account is verified now !")

    return redirect('blog-home')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f"Your account has been created. Verify it on {email}")
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form': form})


@method_decorator(csrf_exempt, name='dispatch')
class UserLikedPostsView(View):
    def get(self, request, id):
        context = [x.id for x in User.objects.get(id=id).likes.all()]
        return JsonResponse(context, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserDisLikedPostsView(View):
    def get(self, request, id):
        context = [x.id for x in User.objects.get(id=id).dislikes.all()]
        return JsonResponse(context, safe=False)

