from django import forms
from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta: # 概要情報
        # フォーム化対象のモデル(テーブル)名。ここにデータが保存される
        model = Topic # 対応するモデル
        fields = ['text'] # 入力対象
        labels = {'text':''} # HTMLでのラベル表示

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text'] # もしここをfields = ['text','topic']にしたら、new_entry()ビュー関数はどう変わる？
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}