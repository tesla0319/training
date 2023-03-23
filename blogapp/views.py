from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogPost

class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'orderby_records'
    queryset = BlogPost.objects.order_by('-posted_at')
    paginate_by = 5

class BlogDetail(DetailView):
    template_name='post.html'
    model = BlogPost

class ScienceView(ListView):
    '''科学カテゴリの記事を一覧表示するビュー
    '''
    # science_list.htmlをレンダリングする
    template_name = 'science_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'science_records'
    # category='science'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class DailylifeView(ListView):
    '''日常カテゴリの記事を一覧表示するビュー
    '''
    # dailylife_list.htmlをレンダリングする
    template_name = 'dailylife_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    # category='dailylife'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2

class MusicView(ListView):
    '''音楽カテゴリの記事を一覧表示するビュー
    '''
    # music_list.htmlをレンダリングする
    template_name = 'music_list.html'
    # クラス変数modelにモデルBlogPostを設定
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'music_records'
    # category='music'のレコードを抽出して
    # 投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    paginate_by = 2
