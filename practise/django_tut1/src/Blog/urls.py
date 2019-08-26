from django.urls import path

from .views import (
    article_create_view,
    article_detail_view,
    article_list_view,
    ArticleListView,
    ArticleDetailView,
)

app_name = 'articles'
urlpatterns = [
    #path('', article_list_view, name='article-list'),
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', article_create_view, name='article-create'),
    #path('<int:id>/', article_detail_view, name='article-detail'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),

    ]