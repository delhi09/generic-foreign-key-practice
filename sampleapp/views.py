from django.shortcuts import render
from django.views import View

from sampleapp.forms import CommentForm
from .models import Photo, Comment
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(View):
    def get(self, request):
        return render(request, "index.html", {})


class PhotoView(View):
    def get(self, request, photo_id):
        photo = Photo.objects.get(id=photo_id)
        return render(
            request,
            "photo.html",
            {
                "photo": photo,
                "form": CommentForm(),
            },
        )


class PhotoCommentView(LoginRequiredMixin, View):
    def post(self, request, photo_id):
        form = CommentForm(request.POST)
        photo = Photo.objects.get(id=photo_id)
        if not form.is_valid():
            return render(
                request,
                "photo.html",
                {
                    "photo": photo,
                    "form": form,
                },
            )
        comment = Comment(
            text=form.cleaned_data["text"],
            content_object=photo,
            posted_by=request.user,
        )
        comment.save()
        return render(
            request,
            "photo.html",
            {
                "photo": photo,
                "form": CommentForm(),
            },
        )
