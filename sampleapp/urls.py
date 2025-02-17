from django.urls import path

from . import views

app_name = "sampleapp"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("photos/<int:photo_id>/", views.PhotoView.as_view(), name="photo"),
    path(
        "photos/<int:photo_id>/comments/",
        views.PhotoCommentView.as_view(),
        name="photo_comments",
    ),
]
