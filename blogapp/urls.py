from django.urls import path
from . import views

# URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name = 'blogapp'

# URLパターンを登録するためのリスト
urlpatterns = [
    # http(s)://ホスト名/以下のパスが''(無し)の場合
    # viewsモジュールのindexViewを実行
    # URLパターン名は'index'
    path('',views.IndexView.as_view(), name='index'),
    
    # リクエストされたURLが「blog-detail/id」の場合
    # viewsモジュールのBlogdetailを実行
    # URLパターン名は'blog_detail'
    path(
        # 詳細ページのURLは「blog-detail/id」
        'blog-detail/<int:pk>/',
        # viewsモジュールのBlogdetailを実行
        views.BlogDetail.as_view(),
        # URLパターン名は'blog_detail'
        name='blog_detail'
        ),
    # sienceカテゴリの一覧ページのURLパターン
    path(
        # scienceカテゴリの一覧ページのURLは「science-list/」
        'science-list/',
        # viewsモジュールのBlogdetailを実行
        views.ScienceView.as_view(),
        # URLパターンの名前を'science_list'にする
        name='science_list'
        ),
    # dailylifeカテゴリの一覧ページのURLパターン
    path(
        # dailylifeカテゴリの一覧ページのURLは「dailylife-list/」
        'dailylife-list/',
        # viewsモジュールのDailylifeViewsを実行
        views.DailylifeView.as_view(),
        # URLパターン名を'dailylife_list'にする
        name='dailylife_list'
        ),
    # musicカテゴリの一覧ページのURLパターン
    path(
        # musicカテゴリの一覧ページのURLは「music-list/」
        'music-list/',
        # viewsモジュールのMusic_viewsを実行
        views.MusicView.as_view(),
        # URLパターンを'music_list'にする
        name='music_list'
        ),
]