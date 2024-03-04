from django.urls import path

from . import views

urlpatterns = [
    # шлях - /polls/, в’юха - views.index, назва в’юхи - “index”
    path("", views.index, name="index"),
    # шлях - /polls/class, в’юха - views.IndexView, назва в’юхи - “class”
    path("class", views.IndexView.as_view(), name="class"),

    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
