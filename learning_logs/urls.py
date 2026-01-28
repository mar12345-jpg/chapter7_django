"""learning_logsのURLパターンの定義"""


from django.urls import path

from learning_logs import views


app_name = 'learning_logs'
urlpatterns = [
    # ホームページ
    # パス文字れる => 関数名,パスに別名を付ける
    # index = ''
    path('',views.index,name='index'),
]