from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic
from django.utils.encoding import smart_str
from wsgiref.util import FileWrapper
import mimetypes
import os

from .models import Profile
from .forms import EditProfileForm
from .forms import SignupForm
from .utils import get_or_create_profile
from penndsg.settings import MEDIA_ROOT


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=raw_password,
            )
            login(request, user)
            return redirect('account:detail')
    else:
        form = SignupForm()
    return render(request, 'account/signup.html', {'form': form})


@login_required
def profile_detail_view(request):
    p = get_or_create_profile(request.user)
    context = {'profile': p}
    return render(request, 'account/detail.html', context)


@login_required
def edit_profile_view(request):
    p = get_or_create_profile(request.user)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=p)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, 'Changes saved successfully'
            )
            return redirect('account:detail')
        else:
            messages.add_message(
                request, messages.ERROR, 'An error occurred'
            )
            return redirect('account:edit')
    else:
        form = EditProfileForm(instance=p)
    context = {'form': form}
    return render(request, 'account/edit.html', context)


@login_required
def download_resume(request):
    try:
        file_path = request.user.profile.resume.name
    except:
        raise Http404("No resume found.")
    # https://stackoverflow.com/q/15246661/2680824
    file_name = os.path.basename(file_path)
    file_path = MEDIA_ROOT + '/' + file_path
    file_wrapper = FileWrapper(open(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = (
        'attachment; filename={}'.format(smart_str(file_name))
    )
    return response
