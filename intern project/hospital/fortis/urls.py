from django.urls import path
from fortis import views

urlpatterns = [
    path("home", views.home, name = "home"),
    path("savetodo", views.savethistodo, name = "savetodo"),
    path("deletethistodo/<int:myid>", views.deletethis),

    path("updatetodo/<int:myid>", views.updatetodo),

    path("updattodonow/<int:myid>", views.updatethisnow),

    path("signuphere", views.signupgere),

    path("loginhere", views.loginfun),

    path("logouthere", views.logouthere),
]
