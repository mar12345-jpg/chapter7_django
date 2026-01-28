"""learning_logsのURLパターンの定義"""

# アプリ内のパス指定
from django.urls import path

from learning_logs import views

# アプリ名を記述
app_name = 'learning_logs'
urlpatterns = [
    # ホームページ
    # パス文字れる => 関数名,パスに別名を付ける
    # learning_logs:index = ''
    # {% url "learning_logs:index" %}
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
]