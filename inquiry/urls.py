from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.inquiry, name="inquiry"), #문의하기
    path("ask", views.ask, name="ask"), #문의 글 작성 페이지
    path("inqdetail/<str:id>", views.inqdetail, name="inqdetail"), #문의 글 자세히 보기 페이지
    path("inqedit/<str:id>", views.inqedit, name="inqedit"), #문의 글 수정 페이지
    path("inqdelete/<str:id>", views.inqdelete, name="inqdelete"), #문의 글 삭제 url
    path("answer", views.answer, name="answer"), #관리자용 문의 리스트 페이지
    path("ansdetail/<str:id>", views.ansdetail, name="ansdetail"), #관리자용 문의 답변 페이지
] 