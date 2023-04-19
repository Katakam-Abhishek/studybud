from django.shortcuts import render
from django.http import HttpResponse


rooms    =   [
    {'id'   :   1, 'name'   :   'Let\'s learn Python'},
    {'id'   :   2, 'name'   :   'Web development'},
    {'id'   :   3, 'name'   :   'Learn Django with me'},
]


# Create your views here.
def home(request):
    context     =   {'rooms':rooms}
    return render(request, 'base/home.html',context)


def room(request, pk):
    room    =   None
    [room := _ for _ in rooms if _['id'] == int(pk)]
    context =   {'room':room}
    return render(request, 'base/room.html', context)