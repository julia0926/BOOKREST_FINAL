from django import forms
from django.db.models import fields
from .models import *

#문의 글 작성 폼
class QInquiryForm(forms.ModelForm):
    class Meta:
        model = QInquiry
        fields = ['title', 'body']
#  'qtype', 
#관리자용 해시태그 추가 폼
class QtypeForm(forms.ModelForm):
    class Meta:
        model = Qtype
        fields = ['type']

#관리자용 문의 답변 작성 폼
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['text']