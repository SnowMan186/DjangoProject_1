from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost

class PostListView(ListView):
    model = BlogPost
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return BlogPost.objects.filter(published=True)

class PostDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views_count += 1
        post.save(update_fields=["views_count"])
        return post

class PostCreateView(CreateView):
    model = BlogPost
    form_class = BlogPost
    template_name = 'blog/post_create.html'
    success_url = '/'

class PostUpdateView(UpdateView):
    model = BlogPost
    fields = '__all__'
    template_name = 'blog/post_update.html'

    def get_success_url(self):
        return reverse('blog:post-detail', args=(self.object.id,))

class PostDeleteView(DeleteView):
    model = BlogPost
    template_name = 'blog/post_confirm_delete.html'
    success_url = '/'
