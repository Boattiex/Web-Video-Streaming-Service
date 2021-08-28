from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from os import listdir
from django_tables2 import RequestConfig
from json_response import JsonResponse
from .models import Livestream
from .tables import MyStreamTable
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'stream/home.html')

def about(request):
    return render(request, 'stream/about.html', {'title': 'About'})

@login_required
def mystream(request):
    if request.method == "POST":
       Livestream.objects.create(key=get_random_string(), user=request.user)

       streamkey = str(Livestream.objects.filter(user = request.user).latest('id')).split(':')[-1]
    if request.method == "GET":
       streamkey = ''

    table = MyStreamTable(Livestream.objects.filter(user = request.user))
    RequestConfig(request).configure(table)

    return render(request, 'stream/mystream.html', {'table': table, 'streamkey': streamkey})

@require_POST
@csrf_exempt
def start_stream(request):
    """ This view is called when a stream starts.
    """
    stream = get_object_or_404(Livestream, key=request.POST["name"])

    # Ban streamers by setting them inactive
    if not stream.user.is_active:
        return HttpResponseForbidden("Inactive user")

    # Don't allow the same stream to be published multiple times
    if stream.started_at:
        return HttpResponseForbidden("Already streaming")

    stream.started_at = timezone.now()
    stream.save()

    # Redirect to the streamer's public username
    return redirect(stream.user.username)
