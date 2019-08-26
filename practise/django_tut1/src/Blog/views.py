from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleModelForm
from .models import Article

from django.views.generic import (
    ListView,
    DetailView,
)
    

# Create your views here.

def article_create_view(request):
    form = ArticleModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleModelForm()
    context = {
        'form': form
    }
    return render(request, "articles/article_create.html", context)

def article_list_view(request):
    querySet = Article.objects.all()
    context = {
        'object_list': querySet
    }
    return render(request, "articles/article_list.html", context)

def article_detail_view(request,id):
    obj = get_object_or_404(Article, id=id)
    context = {
        'object': obj
    }
    return render(request, "articles/article_detail.html", context)

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        print(id_)
        return get_object_or_404(Article, id=id_)