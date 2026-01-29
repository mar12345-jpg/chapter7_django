from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta: # 概要情報
        # フォーム化対象のモデル(テーブル)名。ここにデータが保存される
        model = Topic # 対応するモデル
        fields = ['text'] # 入力対象
        labels = {'text':''} # HTMLでのラベル表示