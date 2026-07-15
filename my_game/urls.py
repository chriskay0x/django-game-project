from django.urls import path
from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("enter/", views.enter, name="enter"),
    path("climb/", views.climb, name="climb"),
    path("walkaway/", views.walkaway, name="walkaway"),
    path("dead/", views.dead, name="dead"),
    path("fight/", views.fight, name="fight"),
    path("left/", views.left, name="left"),
    path("right/", views.right, name="right"),
    path("roof/", views.roof, name="roof"),
    path("run/", views.run, name="run"),
    path("snake/", views.snake, name="snake"),
    path("treasure/", views.treasure, name="treasure"),
    path("window/", views.window, name="window"),
    path("leave/", views.leave, name="leave"),
]
