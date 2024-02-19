from django.urls import path

from . import views

urlpatterns = [
    # шлях - /polls/, в’юха - views.index, назва в’юхи - “index”
    path("", views.index, name="index"),
    # шлях - /polls/class, в’юха - views.IndexView, назва в’юхи - “class”
    path("class", views.IndexView.as_view(), name="class"),
]
