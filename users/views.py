from django.shortcuts import render, redirect
from .models import User
from django.http import Http404
from .forms import UserRegisterForm
from django.contrib import messages


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
