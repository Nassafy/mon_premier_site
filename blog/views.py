from django.shortcuts import render, get_object_or_404
from .models import  Post
from django.utils import timezone
import subprocess
from django.views.generic import View
from django.http import  HttpResponse, HttpResponseRedirect
from .form import CodeForm

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render (request, 'blog/pagelancement.html', {'posts':posts})


def launch_server(request):
    subprocess.call('powerwake 192.168.1.81', shell=True)
    return HttpResponse("Serveur lancer!")


def get_code(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        #data = request.get['code']
        if form.is_valid() and form.cleaned_data['code'] == '78m39':

                subprocess.call('powerwake 192.168.1.81', shell=True)
                return HttpResponseRedirect('/code')

    else:
        form = CodeForm()

    return render(request, 'blog/pagelancement.html', {'form': form})





