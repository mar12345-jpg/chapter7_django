from django.shortcuts import render

from learning_logs.models import Topic

# Create your views here.

def index(request):
    """学習ノートのホームページ"""
    # tenplates/アプリ名フォルダ/を探す
    return render(request,'learning_logs/index.html')

def topics(request):
    """すべてのトピックを表示する"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)