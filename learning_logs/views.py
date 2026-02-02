from django.shortcuts import redirect, render

from learning_logs.forms import TopicForm,EntryForm
from learning_logs.models import Topic, Entry

from django.contrib.auth.decorators import login_required # p248
from django.http import Http404 # p254

# Create your views here.

def index(request):
    """学習ノートのホームページ"""
    # tenplates/アプリ名フォルダ/を探す
    return render(request,'learning_logs/index.html')


@login_required # p248
def topics(request):
    """すべてのトピックを表示する"""
    # トピックテーブルのレコードを日付昇順並べ替えで習得
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # 検索結果に'topics'という名前を付けて辞書に入れてhtmlに渡す
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)

@login_required
def topic(request, topic_id):
    """1つのトピックとそれについてのすべての記事を表示"""
    topic = Topic.objects.get(id=topic_id)
    # トピックが現在のユーザーが所持するものであることを確認する
    if topic.owner != request.user:
        raise Http404

    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
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

@login_required
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
            new_entry = form.save(commit=False) # メモリ上には登録予定のデータは置いてあるけど、ommit=FalseでDBにはまだ入れないでおこう
                                                # フォームの内容を使って モデルインスタンスを作る けれど、そのインスタンスを まだ save() しない
            new_entry.topic = topic
            new_entry.save() # モデルのセーブを呼び出してるよ
            return redirect('learning_logs:topic', topic_id=topic_id)

    # 空または無効のフォームを表示する
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """既存の記事を編集する"""
    entry = Entry.objects.get(id=entry_id) # データベースから指定されたIDのEntryを取得する
    topic = entry.topic # 編集対象の記事が属しているTopicを取得。編集後にリダイレクトするために必要。

    if request.method != 'POST': # リクエストがPOST以外（＝初回アクセス、GET）の場合の処理
        # 初回リクエスト時は現在の記事の内容がフォームに埋め込まれている
        form = EntryForm(instance=entry) # instance=entryを渡すことで「編集フォーム」になる
    else:
        # POSTでデータが送信されたのでこれを処理する
        form = EntryForm(instance=entry, data=request.POST) # instance=entryを渡すことで「既存のentryを更新する」動作になる
        if form.is_valid(): # フォームの入力内容がバリデーションを通ったかチェック
            form.save() # フォームの内容をデータベースに保存（既存entryの更新）
            return redirect('learning_logs:topic', topic_id=topic.id) # 編集が終わったら、その記事が属するTopicのページへリダイレクト
                                                                      # ユーザーに「編集完了後の画面」を見せるため
    context = {'entry': entry, 'topic': topic, 'form': form} # entry（編集対象）、topic（親）、form（フォーム）

    return render(request, 'learning_logs/edit_entry.html', context)
    # テンプレートを描画してユーザーに返す・GET の場合は「編集フォーム表示」・POST でエラーがあった場合は「エラー付きフォーム再表示」

