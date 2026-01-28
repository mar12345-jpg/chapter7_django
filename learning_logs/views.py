from django.shortcuts import render

# Create your views here.

def index(request):
    """学習ノートのホームページ"""
    # tenplates/アプリ名フォルダ/を探す
    return render(request,'learning_logs/index.html')