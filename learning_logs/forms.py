from django import forms
from .models import Topic

class ToppicForm(forms.ModelForm):
    class Meta:
        model = Topic # 対応するモデル(テーブル)名
        fields = ['text'] # 入力対象
        labels = {'text':''} # HTMLでのラベル表示