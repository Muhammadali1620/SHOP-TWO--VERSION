from django.shortcuts import redirect, render
from django.contrib import messages
from apps.comments.forms import CommentCreateForm
from apps.products.services import change_product_avg_rating


def add_comment(request, pk):
    if request.method != 'POST':
        return redirect(request.META['HTTP_REFERER'])
    print(request.POST)
    form = CommentCreateForm(request.POST)

    if not form.is_valid():
        messages.error(request, form.errors)
        return redirect(request.META['HTTP_REFERER'])
    form.save()
    change_product_avg_rating(product_id=pk)
    return redirect(request.META['HTTP_REFERER'])