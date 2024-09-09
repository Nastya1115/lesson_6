from django.urls import path
import blog.views as views

urlpatterns = [
    path("", views.blogs_list, name="blogs_list")
]