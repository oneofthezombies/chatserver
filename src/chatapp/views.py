from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse


def index(request):
    return render(request, 'chatapp/index.html')


def join(request):
    try:
        room_name = request.POST['room-name']
    except KeyError:
        raise Http404()
    else:
        return HttpResponseRedirect(reverse('chatapp:room', args=(room_name,)))


def room(request, room_name):
    return render(request, 'chatapp/room.html', {
        'room_name': room_name
    })
