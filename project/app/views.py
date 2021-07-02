from django.shortcuts import render


def index(req):
    return render(req, "index.html")


def room(req, room_name):
    return render(req, "room.html", {"room_name": room_name})
