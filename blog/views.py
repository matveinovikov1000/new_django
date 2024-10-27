from django.views.generic import (
    TemplateView,
    DetailView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy, reverse
from blog.models import BlogPost


class BlogDetailView(DetailView):
    model = BlogPost

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogListView(ListView):
    model = BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(publication_sign=True)


class BlogCreateView(CreateView):
    model = BlogPost
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:posts")


class BlogUpdateView(UpdateView):
    model = BlogPost
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:posts")

    def get_success_url(self):
        return reverse("blog:post", args=[self.kwargs.get("pk")])


class BlogDeleteView(DeleteView):
    model = BlogPost
    success_url = reverse_lazy("blog:posts")


class BaseTemplateView(TemplateView):
    template_name = "blog/base.html"
