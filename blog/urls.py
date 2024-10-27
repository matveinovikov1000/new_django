from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    BlogDetailView,
    BlogListView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BaseTemplateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post"),
    path("posts/", BlogListView.as_view(), name="posts"),
    path("create/", BlogCreateView.as_view(), name="create_blog"),
    path("<int:pk>/update/", BlogUpdateView.as_view(), name="update_blog"),
    path("<int:pk>/delete/", BlogDeleteView.as_view(), name="delete_blog"),
    path("base/", BaseTemplateView.as_view(), name="base"),
]
