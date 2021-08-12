from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.

#views for register

#문의 목록 페이지
def inquiry(request):
    inquirys = QInquiry.objects
    return render(request, 'inquiry.html', {'inquirys':inquirys})

#문의 글 작성 페이지
def ask(request):
    if request.method == 'POST':
        form = QInquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.pub_date = timezone.now()
            inquiry.save()
            form.save_m2m()
            return redirect('inquiry')
    else:
        form = QInquiryForm()
        return render(request, 'ask.html', {'form' : form})
    
#작성 글 자세히 보기
def inqdetail(request, id):
    inquiry = get_object_or_404(QInquiry, id = id)
    return render(request, 'inqdetail.html', {'inquiry':inquiry})

#작성 글 수정하기
def inqedit(request, id):
    inquiry = get_object_or_404(QInquiry, id = id)
    if request.method == 'POST':
        form = QInquiryForm(request.POST, instance=inquiry)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.pub_date = timezone.now()
            inquiry.save()
            form.save_m2m()
            return redirect('inqdetail', id)
    else:
        form = QInquiryForm(instance=inquiry)
        return render(request, 'inqedit.html', {'form' : form})

#작성 글 삭제하기
def inqdelete(request, id):
    inquiry = get_object_or_404(QInquiry, id = id)
    inquiry.delete()
    return redirect('inquiry')

#views for admin

#관리자용 문의글 목록 페이지
def answer(request):
    inquirys = QInquiry.objects
    return render(request, 'answer.html', {'inquirys':inquirys})

#관리자용 문의 답변 페이지
def ansdetail(request, id):
    inquiry = get_object_or_404(QInquiry, id = id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit = False)
            answer.ask_id = inquiry
            answer.text = form.cleaned_data['text']
            answer.save()
            return redirect('ansdetail', id)

    else:
        form = AnswerForm()
        return render(request, 'ansdetail.html', {'inquiry':inquiry, 'form':form})