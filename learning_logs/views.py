from django.shortcuts import redirect, render

from learning_logs.forms import TopicForm
from learning_logs.models import Topic

# Create your views here.

def index(request):
    """学習ノートのホームページ"""
    # tenplates/アプリ名フォルダ/を探す
    return render(request,'learning_logs/index.html')


def topics(request):
    """すべてのトピックを表示する"""
    # トピックテーブルのレコードを日付昇順並べ替えで習得
    topics = Topic.objects.order_by('date_added')
    # 検索結果に'topics'という名前を付けて辞書に入れてhtmlに渡す
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

def topic(request, topic_id):
    """1つのトピックとそれについてのすべての記事を表示"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """新規トピックを追加する"""
    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = TopicForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')

    # 空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)