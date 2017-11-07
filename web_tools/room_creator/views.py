from django.shortcuts import render


def index(request):
    return render(request, 'room_creator/draw_room.html')
