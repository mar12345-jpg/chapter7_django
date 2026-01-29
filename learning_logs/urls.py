"""learning_logsのURLパターンの定義"""

# アプリ内のパス指定
from django.urls import path

from learning_logs import views

# アプリ名を記述
app_name = 'learning_logs'
urlpatterns = [
    # ホームページ
    path('', views.index, name='index'),
    # パス文字れる => 関数名,パスに別名を付ける
    # learning_logs:index = ''
    # {% url "learning_logs:index" %}
    # すべてのトピックを表示するページ
    path('topics/', views.topics, name='topics'),
    # 個別トピックの詳細ページ
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 新規トピックの追加ページ
    path('new_topic/', views.new_topic, name='new_topic'),
    # 新規記事の追加ページ 引数パスにトピックIDをセット
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]