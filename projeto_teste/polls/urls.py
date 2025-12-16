from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post_new/", views.post_new, name="post_new"),
    path("post_view/<int:pk>/", views.post_view, name="post_view"),
]