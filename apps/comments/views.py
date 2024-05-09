from django.shortcuts import redirect, render
from django.contrib import messages
from apps.comments.forms import CommentCreateForm


def add_comment(request, pk):
    if request.method != 'POST':
        return redirect(request.META['HTTP_REFERER'])
    form = CommentCreateForm(request.POST)

    if not form.is_valid():
        messages.error(request, form.errors)
        return redirect(request.META['HTTP_REFERER'])
    form.save()
    return redirect(request.META['HTTP_REFERER'])