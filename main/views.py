from django.core import paginator
from django.shortcuts import render,get_object_or_404
from category.models import BookClassInfo
from django.core.paginator import Paginator
import random
# Create your views here.


def main(request):
    books = BookClassInfo.objects.all()
    sort_val = books

    ranNum = random.randrange(0, 4)
    if ranNum == 0:
        major_list = BookClassInfo.objects.filter(department='인문융합자율학부')
        major = "인문융합자율학부"
        sort_val = major_list
    if ranNum == 1:
        major_list = BookClassInfo.objects.filter(department='사회융합자율학부')
        major="사회융합자율학부"
        sort_val = major_list
    if ranNum == 2:
        major_list = BookClassInfo.objects.filter(department='미디어콘텐츠융합자율학부')
        major="미디어콘텐츠융합자율학부"
        sort_val = major_list
    if ranNum == 3:
        major_list = BookClassInfo.objects.filter(department='IT융합자율학부')
        major="IT융합자율학부"
        sort_val = major_list

    paginator = Paginator(sort_val, 8)
    book_list = paginator.get_page(1)  # posts

    return render(request, 'main.html', {'book_list': book_list, 'major': major})


def noticeBase(request):
    return render(request, 'noticeBase.html')


def detail(request, id):
    book = get_object_or_404(BookClassInfo, id = id)
    return render(request, 'detail.html', {'book':book})
