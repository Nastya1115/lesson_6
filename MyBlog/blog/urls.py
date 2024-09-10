from django.urls import path
import blog.views as views

urlpatterns = [
    path("", views.blogs_list, name="blogs_list"),
    path("post/<int:post_id>", views.post_show, name='post'),
]