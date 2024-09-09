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
