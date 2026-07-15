from django.shortcuts import render

# Create your views here.
def climb(request):
    return render(request, "game/climb.html")

def dead(request):
    return render(request, "game/dead.html")

def enter(request):
    return render(request, "game/enter.html")

def fight(request):
    return render(request, "game/fight.html")

def leave(request):
    return render(request, "game/leave.html")

def left(request):
    return render(request, "game/left.html")

def right(request):
    return render(request, "game/right.html")

def roof(request):
    return render(request, "game/roof.html")

def run(request):
    return render(request, "game/run.html")

def snake(request):
    return render(request, "game/snake.html")

def start(request):
    return render(request, "game/start.html")

def treasure(request):
    return render(request, "game/treasure.html")

def walkaway(request):
    return render(request, "game/walkaway.html")

def window(request):
    return render(request, "game/window.html")