from django.shortcuts import render
from django.http import HttpResponse
from blog.models import *

# Create your views here.


def blogs_list(request):
    blogs = Post.objects.all()
    context = {
        "blogs_list": blogs,
    }
    return render(
        request,
        template_name="post_list.html",
        context=context
    )

def post_show(request, post_id):
    post_obj = Post.objects.get(id=post_id)
    print(post_obj)
    context = {
        "post_obj": post_obj,
    }

    return render(
        request,
        template_name="post_show.html",
        context=context,
    )