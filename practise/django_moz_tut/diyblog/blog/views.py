from django.views import generic
from django.shortcuts import render, get_object_or_404
from blog.models import Blog, BlogAuthor, BlogComment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse


def index(request):
    num_blogs = Blog.objects.all().count()
    num_authors = BlogAuthor.objects.all().count()
    context = {
        'num_blogs': num_blogs,
        'num_authors': num_authors,
    }
    return render(request, 'index.html', context)


class BlogListView(generic.ListView):
    model = Blog
    paginate_by = 5


class BloggerListView(generic.ListView):
    model = BlogAuthor
    paginate_by = 5


class BlogListbyAuthorView(generic.ListView):
    model = Blog
    paginate_by = 5
    template = 'blog/blog_list_by_author.html'

    def get_queryset(self):
        id = self.kwargs['pk']
        target_author = get_object_or_404(BlogAuthor, pk=id)
        return Blog.objects.filter(author=target_author)

    def get_context_data(self, **kwargs):
        context = super(BlogListbyAuthorView, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context


class BlogDetailView(generic.DetailView):
    model = Blog
    template = 'blog/blog_detail.html'


class BlogCommentCreate(LoginRequiredMixin, CreateView):
    model = BlogComment
    fields = ['description', ]

    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk'], })
