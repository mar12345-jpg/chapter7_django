from django.shortcuts import redirect, render

from learning_logs.forms import TopicForm,EntryForm
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
            # /topics/
            return redirect('learning_logs:topics')

    # 空または無効のフォームを表示する
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    """特定のトピックに新規記事を追加する"""
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        # データは送信されていないので空のフォームを生成する
        form = EntryForm()
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # 空または無効のフォームを表示する
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)